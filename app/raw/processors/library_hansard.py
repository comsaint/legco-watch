# -*- coding: utf-8 -*-
"""
Processor for Hansard
"""
import logging
from raw.models import RawCouncilHansard, LANG_BOTH, LANG_EN, LANG_CN
from raw.processors.base import BaseProcessor, file_wrapper
from django.db.models import Count
from django.core.exceptions import *
from django.utils.timezone import now
import warnings
import re
from raw import utils


logger = logging.getLogger('legcowatch')


class LibraryHansardProcessor(BaseProcessor):
    """
    Class that handles the loading of Library Hansard scraped items 
    into RawCouncilHansard table
    """
    def process(self, *args, **kwargs):
        logger.info("Processing file {}".format(self.items_file_path))
        counter = 0
        for item in file_wrapper(self.items_file_path):
            counter += 1
            if item['type'] == 'LibraryResultPage':
                # Ignore these entries
                continue
            if item['type'] == 'LibraryHansard':
                self._process_hansard_item(item)
        # After all downloaded hansards are created/updated, merge the ones that are parts of a hansard.
        self._merge_parts()
        logger.info("{} (raw) items processed, {} created, {} updated, {} warnings".format(counter, self._count_created, self._count_updated, self._count_warning))
        logger.info("{} merged items created/updated.".format(self._count_merged))
        
    def _process_hansard_item(self, item):
        # Usually generate three items, floor record and EN/CN formal records
        # but can be more or less
        # Ancient hansards may contain an English version and an image, probably not even an image
        # The first Chinese hansard seems to exist on 1985.10.30
        # Old harsards are bilingual (2 files), without floor version. 
        # Floor version seems to exist since 1995.10.12
        
        # Loop over files in an item
        #print(u"Processing item: {}".format(item['title_en']))
        for i in range(len(item['links'])):
            # clear variables
            date_str = None
            lang = None
            language = None
            uid = None
            title = None
            url = None
            local_filename = None
            obj = None
            
            #Date always the same for an item
            date_str = self._get_date(item)
            if 'English' in item['links'][i][0]:
                #A formal, English record
                lang = u'e'
                language = LANG_EN
            elif u'中文' in item['links'][i][0]:
                lang = u'c'
                language = LANG_CN
            elif 'Floor' in item['links'][i][0]:
                lang = u'b'
                language = LANG_BOTH
            elif 'Image' in item['links'][i][0]:
                # we do not do images
                continue
            else:
                # Assume they are new Floor versions, log a warning just in case
                logger.warn(u'Unrecognised type: {}. Assume floor records.'.format(item['links'][i][0]))
                self._count_warning+=1
                lang = u'b'
                language = LANG_BOTH
            
            # Be careful of potential 'Parts' in title
            title = item['links'][i][0] #e.g. "H20150325 (Floor Version)"
            
            # Generate an uid
            uid = self._generate_base_hansard_uid(title,date_str,lang)
            if uid is None:
                logger.warn(u'Cannot generate uid for item with title: {}.'.format(title.strip()))
                self._count_warning+=1
                continue
            
            # Put items here for clarity
            #raw_date = date_str
            #language = language # 0,1 or 2
            url = item['links'][i][1]
            local_filename = self._get_local_filename(url, item) #"full/..."
            # Sometimes the file
            
            if local_filename is None:
                # Sometimes due to bandwidth/connection, file may fail to be downloaded
                logger.warn(u'Problem with local_filename of item: {}\nLink: {}'.format(title,url))
                self._count_warning+=1
            
            # Get/Create object from database
            #print(u'Building item: {}'.format(uid))
            # we allow non-unique UID for parts of Hansard, but title should be unique
            # we will merge parts of Hansard into one and create a new instance
            obj = self._get_or_create_hansard_record_by_title(title,uid)
            #if obj is not None:
            # at the moment we do not deal with floor recordings
            if obj is not None and language!=LANG_BOTH:
                obj = self._build_obj(obj, title, date_str, language, url, local_filename, item)
                obj.save()
            #End of for loop
        
        
    def _merge_parts(self):
        # Search for non-unique UIDs, merge their DOCXs into one HTML file, and make a new object for it.
        ## Remember to set the field CREATED_BY_PARTS to True
        # Get the list of duplicate UIDs
        dup_hansard_uid = RawCouncilHansard.objects.values('uid').annotate(uid_count=Count('uid')).exclude(uid_count=1)
        for item in dup_hansard_uid:
            # Firstly, check if we need to merge docs. Sometimes the parts are just appendices,
            # which we will ignore. In this case, there should be a normal UID for this object (without 'p').
            normal_uid = item['uid'].replace('p','')
            try:
                normal_han = RawCouncilHansard.objects.get(uid=normal_uid)
                #print normal_han
                if normal_han.created_by_parts is False:
                    # The parts are appendices. Do not process them.
                    # if this condition is not matched, the program will continue, as we will update the old object
                    continue
            except MultipleObjectsReturned:
                # Usually there should be no MultipleObjectsReturned exception.
                # This is for a very special case on 2012.06.14
                continue
            except ObjectDoesNotExist:
                # We need to create a new object
                pass

            self._count_merged += 1
            print(u'Merging Hansard Parts {}'.format(normal_uid))
            # We have to either create/update the Hansard
            # get a list of hansard objects
            han_part = RawCouncilHansard.objects.filter(uid=item['uid']).order_by('uid') #very weird, order by uid works but title does not
            # get their full local filepaths
            path_list = []
            for han in han_part:
                path_list.append(han.full_local_filename())
            # Make a name for output path, and create a full absolute path for saving
            html_name = han_part[0].uid + '-merge'
            out_htmlpath = han_part[0].full_local_filename().rsplit('/',1)[0] + '/' + html_name
            # Also make a relative path in same format as other normal objects
            local_filepath = '/'.join(out_htmlpath.rsplit('/',2)[1:])
            # Pass the list to merger, and let it write out a file
            html_str_or_None = utils.merge_docx(docx_list=path_list, out_htmlpath=out_htmlpath)
            # Sometimes the DOC/DOCX to HTML conversion fails.
            # In this case, we cannot parse the hansard anyway, so we leave the parts as is.
            if html_str_or_None is None:
                print(u'DOC/DOCX to HTML conversion failed for Hansard parts {}'.format(normal_uid))
            else:
                # Get/Create an object for merged file
                obj,_ = RawCouncilHansard.objects.get_or_create(uid=normal_uid)
                obj.raw_date = han_part[0].raw_date
                obj.language = han_part[0].language
                obj.url = ''
                obj.local_filename = local_filepath
                obj.crawled_from = ''
                obj.last_parsed = now()
                if han_part[0].language == LANG_CN:
                    obj.title = 'H'+ han_part[0].raw_date+' '+u'(中文版)'+u'MERGE'
                else:
                    obj.title = 'H'+ han_part[0].raw_date+' '+u'(English Version)'+u'MERGE'
                # Do not forget this
                obj.created_by_parts = True
                obj.save()

    def _build_obj(self, obj, title, raw_date, language, url, local_file, item):
        obj.title = title
        obj.raw_date = raw_date
        obj.language = language
        obj.url = url
        obj.local_filename = local_file
        obj.crawled_from = item['source_url']
        obj.last_parsed = now()
        if self.job:
            obj.last_crawled = self.job.completed
        return obj


    def _get_or_create_hansard_record_by_uid(self, uid):
        try:
            obj = RawCouncilHansard.objects.get(uid=uid)
            self._count_updated += 1
        except RawCouncilHansard.DoesNotExist:
            obj = RawCouncilHansard(uid=uid)
            self._count_created += 1
        except RawCouncilHansard.MultipleObjectsReturned:
            warnings.warn(u"Found more than one item with raw id {}".format(uid), RuntimeWarning)
            obj = None
        return obj


    def _get_or_create_hansard_record_by_title(self,title,uid):
        try:
            obj = RawCouncilHansard.objects.get(title=title)
            self._count_updated += 1
        except RawCouncilHansard.DoesNotExist:
            obj = RawCouncilHansard(title=title,uid=uid)
            self._count_created += 1
        return obj
    
    
    def _get_local_filename(self, link, item):
        """
        Given a link and an item to which the link belongs, get the local file path that
        matches the link
        """
        # Sanity check, in case of incorrect index order
        for f in item['files']:
            if link == f['url']:
                return f['path']
        return None
    

    def _generate_base_hansard_uid(self, title, date, lang):
        """
        Try to generate a unique id for a harsard item
        e.g.: council_hansard-19950110-e or council_hansard-20100110-b
        or : council_hansard-20120629-p2-e
        Basically council_hansard-<date: YYYYMMDD>-(optional:-p<d>-)<lang>
        e for English, c for Chinese, b for bilingual
        """
        # Handle Hansards divided into parts
        #part = None
        #part_pattern = ur'第(?P<part>.)部分' if lang==u'c' else r'Part (?P<part>.)'
        
        
        #match = re.match(part_pattern,title)
        #if match is not None:
        #    # this hansard is a part
        #    logger.info(u'Title "{}" is a part.'.format(title))
        #    part = match.group('part')
        #    if lang == u'c':
        #        if part == u'一':
        #            part = '1'
        #        elif part == u'二':
        #            part = '2'
        #        elif part == u'三':
        #            part = '3'
        #        else:
        #            logger.error(u"Unknown part character '{}' for hansard title: {}".format(part,title))
        #            part = None
        
        #if date and lang and part:
        #    return u'council_hansard-{}-p{}-{}'.format(date,part,lang)
        #elif date and lang:
        #    return u'council_hansard-{}-{}'.format(date,lang)
        #else:
        #    return None
        
        title_len_max = 16 if lang == u'c' else 28 #allow for 1 extra char
        if len(title.strip())>title_len_max:
            # This is a part file. Put a special char 'p' to indicate.
            return u'council_hansard-{}p-{}'.format(date,lang)
        elif date and lang:
            return u'council_hansard-{}-{}'.format(date,lang)
        else:
            return None
        

    def _get_date(self,item):
        """
        Returns the date string of an item in format YYYYMMDD
        """
        # Some rare cases the title e.g. H20070430 xxxxx is not in format,
        # so we get date from long title.
        return item['title_en'][-11:].replace('.', '')