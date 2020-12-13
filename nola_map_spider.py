from scrapy import Spider, Request
from nola_map.items import NolaMapItem
import pandas as pd
import re



class NolaMapSpider(Spider):
    name = 'nola_map_spider'
    allowed_domains = ['qpublic.net'] # check this 
    start_urls = ['http://qpublic9.qpublic.net/la_orleans_display.php?KEY=1-NPETERSST'] # first url on list

    def parse(self, response):

        urls = open('tract_2200_urls.csv','r+')
        urls = urls.readlines() # read in list
        rem=[x for x in urls] # remove \n
        urls=[rem[y].replace('\n','') for y in range(len(rem))]
        # marigny_urls = pd.read_csv('marigny_urls.csv',header=None) # import into df
        # marigny_urls = marigny_urls[0].tolist() # list of urls
        for url in urls: 
            yield Request(url=url, callback=self.parse_result_page) # parse response

    def parse_result_page(self, response):
        # if statement: if this comes up blank, skip, give null for every field
        if len(response.xpath('//body/text()').extract()) == 1: # scrapes list "no data available"
            owner_name_ln1 = 'empty'
            owner_name_ln2 = 'empty'
            owner_name_ln3 = 'empty'
            owner_name_ln4 = 'empty'
            owner_name_ln5 = 'empty'
            owner_name_ln6 = 'empty'
            owner_name_ln7 = 'empty'
            owner_name_ln8 = 'empty'
            owner_name_ln9 = 'empty'
            owner_name_ln10 = 'empty'
            owner_name_ln11 = 'empty'
            owner_name_ln12 = 'empty'
            owner_name_ln13 = 'empty'
            owner_name_ln14 = 'empty'
            owner_name_ln15 = 'empty'
            scrape_date = 'empty'
            owner_addr_ln1 = 'empty'
            owner_addr_ln2 = 'empty'
            owner_addr_ln3 = 'empty'
            owner_addr_ln4 = 'empty'
            owner_addr_ln5 = 'empty'
            owner_addr_ln6 = 'empty'
            municipal_dist = 'empty'
            location_addr = 'empty'
            tax_bill_num = 'empty'
            subdivision_name = 'empty'
            land_area = 'empty'
            building_area = 'empty'
            square = 'empty'
            revised_bldg_area = 'empty'
            n2021_land_val = 'empty'
            n2021_bldg_val = 'empty'
            n2021_total_val = 'empty'
            n2021_assd_land_val = 'empty'
            n2021_assd_bldg_val = 'empty'
            n2021_total_assd_val = 'empty'
            n2021_hmsd_ex_val = 'empty'
            n2021_tax_assmt = 'empty'
            n2020_land_val = 'empty'
            n2020_bldg_val = 'empty'
            n2020_total_val = 'empty'
            n2020_assd_land_val = 'empty'
            n2020_assd_bldg_val = 'empty'
            n2020_total_assd_val = 'empty'
            n2020_hmsd_ex_val = 'empty'
            n2020_tax_assmt = 'empty'
            n2019_land_val = 'empty'
            n2019_bldg_val = 'empty'
            n2019_total_val = 'empty'
            n2019_assd_land_val = 'empty'
            n2019_assd_bldg_val = 'empty'
            n2019_total_assd_val = 'empty'
            n2019_hmsd_ex_val = 'empty'
            n2019_tax_assmt = 'empty'

            item = NolaMapItem()
            item['owner_name_ln1'] = owner_name_ln1
            item['owner_name_ln2'] = owner_name_ln2
            item['owner_name_ln3'] = owner_name_ln3
            item['owner_name_ln4'] = owner_name_ln4
            item['owner_name_ln5'] = owner_name_ln5
            item['owner_name_ln6'] = owner_name_ln6
            item['owner_name_ln7'] = owner_name_ln7
            item['owner_name_ln8'] = owner_name_ln8
            item['owner_name_ln9'] = owner_name_ln9
            item['owner_name_ln10'] = owner_name_ln10
            item['owner_name_ln11'] = owner_name_ln11
            item['owner_name_ln12'] = owner_name_ln12
            item['owner_name_ln13'] = owner_name_ln13
            item['owner_name_ln14'] = owner_name_ln14
            item['owner_name_ln15'] = owner_name_ln15
            item['scrape_date'] = scrape_date
            item['owner_addr_ln1'] = owner_addr_ln1
            item['owner_addr_ln2'] = owner_addr_ln2
            item['owner_addr_ln3'] = owner_addr_ln3
            item['owner_addr_ln4'] = owner_addr_ln4
            item['owner_addr_ln5'] = owner_addr_ln5
            item['owner_addr_ln6'] = owner_addr_ln6
            item['municipal_dist'] = municipal_dist
            item['location_addr'] = location_addr
            item['tax_bill_num'] = tax_bill_num
            item['subdivision_name'] = subdivision_name
            item['land_area'] = land_area
            item['building_area'] = building_area
            item['square'] = square
            item['revised_bldg_area'] = revised_bldg_area
            item['n2021_land_val'] = n2021_land_val
            item['n2021_bldg_val'] = n2021_bldg_val
            item['n2021_total_val'] = n2021_total_val
            item['n2021_assd_land_val'] = n2021_assd_land_val
            item['n2021_assd_bldg_val'] = n2021_assd_bldg_val
            item['n2021_total_assd_val'] = n2021_total_assd_val
            item['n2021_hmsd_ex_val'] = n2021_hmsd_ex_val
            item['n2021_tax_assmt'] = n2021_tax_assmt
            item['n2020_land_val'] = n2020_land_val
            item['n2020_bldg_val'] = n2020_bldg_val
            item['n2020_total_val'] = n2020_total_val
            item['n2020_assd_land_val'] = n2020_assd_land_val
            item['n2020_assd_bldg_val'] = n2020_assd_bldg_val
            item['n2020_total_assd_val'] = n2020_total_assd_val
            item['n2020_hmsd_ex_val'] = n2020_hmsd_ex_val
            item['n2020_tax_assmt'] = n2020_tax_assmt
            item['n2019_land_val'] = n2019_land_val
            item['n2019_bldg_val'] = n2019_bldg_val
            item['n2019_total_val'] = n2019_total_val
            item['n2019_assd_land_val'] = n2019_assd_land_val
            item['n2019_assd_bldg_val'] = n2019_assd_bldg_val
            item['n2019_total_assd_val'] = n2019_total_assd_val
            item['n2019_hmsd_ex_val'] = n2019_hmsd_ex_val
            item['n2019_tax_assmt'] = n2019_tax_assmt

            yield item

        # if it doesn't come up blank, scrape:
        elif len(response.xpath('//body/text()').extract()) == 2:

            lst = response.xpath('//td[@class="owner_value"]/text()').extract()
            # scraping date, "Today's date" on website: CHANGE BELOW
            # marigny is municipal district 3: CHANGE BELOW
            datei = lst.index('\xa0July 26, 2020\xa0') #CHANGE -- THEIR CLOCK IS 6+ hours ahead!!
            munii = lst.index('\xa03\xa0') #CHANGE


            # scrape owner names: possibility of up to 15 names

            owner_name_ln1 = lst[0]

            if datei <= 1:
                owner_name_ln2 = 'n_a'
            else:
                owner_name_ln2 = lst[1]

            if datei <= 2:
                owner_name_ln3 = 'n_a'
            else:
                owner_name_ln3 = lst[2]

            if datei <= 3:
                owner_name_ln4 = 'n_a'
            else:
                owner_name_ln4 = lst[3]

            if datei <= 4:
                owner_name_ln5 = 'n_a'
            else:
                owner_name_ln5 = lst[4]

            if datei <= 5:
                owner_name_ln6 = 'n_a'
            else:
                owner_name_ln6 = lst[5]

            if datei <= 6:
                owner_name_ln7 = 'n_a'
            else:
                owner_name_ln7 = lst[6]

            if datei <= 7:
                owner_name_ln8 = 'n_a'
            else:
                owner_name_ln8 = lst[7]

            if datei <= 8:
                owner_name_ln9 = 'n_a'
            else:
                owner_name_ln9 = lst[8]

            if datei <= 9:
                owner_name_ln10 = 'n_a'
            else:
                owner_name_ln10 = lst[9]

            if datei <= 10:
                owner_name_ln11 = 'n_a'
            else:
                owner_name_ln11 = lst[10]

            if datei <= 11:
                owner_name_ln12 = 'n_a'
            else:
                owner_name_ln12 = lst[11]

            if datei <= 12:
                owner_name_ln13 = 'n_a'
            else:
                owner_name_ln13 = lst[12]

            if datei <= 13:
                owner_name_ln14 = 'n_a'
            else:
                owner_name_ln14 = lst[13]

            if datei <= 14:
                owner_name_ln15 = 'n_a'
            else:
                owner_name_ln15 = lst[14]

            scrape_date = lst[datei] 

            # scrape for owner addresses; possibility for up to 6 lines

            owner_addr_ln1 = lst[datei+1]

            if (datei+2) >= munii:
                owner_addr_ln2 = 'n_a'
            else:
                owner_addr_ln2 = lst[datei+2]

            if (datei+3) >= munii:
                owner_addr_ln3 = 'n_a'
            else:
                owner_addr_ln3 = lst[datei+3]

            if (datei+4) >= munii:
                owner_addr_ln4 = 'n_a'
            else:
                owner_addr_ln4 = lst[datei+4]

            if (datei+5) >= munii:
                owner_addr_ln5 = 'n_a'
            else:
                owner_addr_ln5 = lst[datei+5]

            if (datei+6) >= munii:
                owner_addr_ln6 = 'n_a'
            else:
                owner_addr_ln6 = lst[datei+6]

            municipal_dist = lst[munii]
            location_addr = lst[munii+1]
            tax_bill_num = lst[munii+2]
            subdivision_name = lst[munii+6]
            land_area = lst[munii+7]
            if lst[munii+8] != '\xa0  Viewer not available \xa0':
                building_area = lst[munii+8]
                square = lst[munii+9]
                revised_bldg_area = lst[munii+10]
            else:
                building_area = lst[munii+9]
                square = lst[munii+10]
                revised_bldg_area = lst[munii+11]

            n2021_land_val = response.xpath('//td[@class="tax_value"]/text()').extract()[2]
            n2021_bldg_val = response.xpath('//td[@class="tax_value"]/text()').extract()[3]
            n2021_total_val = response.xpath('//td[@class="tax_value"]/text()').extract()[4]
            n2021_assd_land_val = response.xpath('//td[@class="tax_value"]/text()').extract()[5]
            n2021_assd_bldg_val = response.xpath('//td[@class="tax_value"]/text()').extract()[6]
            n2021_total_assd_val = response.xpath('//td[@class="tax_value"]/text()').extract()[7]
            n2021_hmsd_ex_val = response.xpath('//td[@class="tax_value"]/text()').extract()[8]
            n2021_tax_assmt = response.xpath('//td[@class="tax_value"]/text()').extract()[9]
            n2020_land_val = response.xpath('//td[@class="tax_value"]/text()').extract()[18]
            n2020_bldg_val = response.xpath('//td[@class="tax_value"]/text()').extract()[19]
            n2020_total_val = response.xpath('//td[@class="tax_value"]/text()').extract()[20]
            n2020_assd_land_val = response.xpath('//td[@class="tax_value"]/text()').extract()[21]
            n2020_assd_bldg_val = response.xpath('//td[@class="tax_value"]/text()').extract()[22]
            n2020_total_assd_val = response.xpath('//td[@class="tax_value"]/text()').extract()[23]
            n2020_hmsd_ex_val = response.xpath('//td[@class="tax_value"]/text()').extract()[24]
            n2020_tax_assmt = response.xpath('//td[@class="tax_value"]/text()').extract()[25]
            n2019_land_val = response.xpath('//td[@class="tax_value"]/text()').extract()[34]
            n2019_bldg_val = response.xpath('//td[@class="tax_value"]/text()').extract()[35]
            n2019_total_val = response.xpath('//td[@class="tax_value"]/text()').extract()[36]
            n2019_assd_land_val = response.xpath('//td[@class="tax_value"]/text()').extract()[37]
            n2019_assd_bldg_val = response.xpath('//td[@class="tax_value"]/text()').extract()[38]
            n2019_total_assd_val = response.xpath('//td[@class="tax_value"]/text()').extract()[39]
            n2019_hmsd_ex_val = response.xpath('//td[@class="tax_value"]/text()').extract()[40]
            n2019_tax_assmt = response.xpath('//td[@class="tax_value"]/text()').extract()[41]   


            item = NolaMapItem()
            item['owner_name_ln1'] = owner_name_ln1
            item['owner_name_ln2'] = owner_name_ln2
            item['owner_name_ln3'] = owner_name_ln3
            item['owner_name_ln4'] = owner_name_ln4
            item['owner_name_ln5'] = owner_name_ln5
            item['owner_name_ln6'] = owner_name_ln6
            item['owner_name_ln7'] = owner_name_ln7
            item['owner_name_ln8'] = owner_name_ln8
            item['owner_name_ln9'] = owner_name_ln9
            item['owner_name_ln10'] = owner_name_ln10
            item['owner_name_ln11'] = owner_name_ln11
            item['owner_name_ln12'] = owner_name_ln12
            item['owner_name_ln13'] = owner_name_ln13
            item['owner_name_ln14'] = owner_name_ln14
            item['owner_name_ln15'] = owner_name_ln15
            item['scrape_date'] = scrape_date
            item['owner_addr_ln1'] = owner_addr_ln1
            item['owner_addr_ln2'] = owner_addr_ln2
            item['owner_addr_ln3'] = owner_addr_ln3
            item['owner_addr_ln4'] = owner_addr_ln4
            item['owner_addr_ln5'] = owner_addr_ln5
            item['owner_addr_ln6'] = owner_addr_ln6
            item['municipal_dist'] = municipal_dist
            item['location_addr'] = location_addr
            item['tax_bill_num'] = tax_bill_num
            item['subdivision_name'] = subdivision_name
            item['land_area'] = land_area
            item['building_area'] = building_area
            item['square'] = square
            item['revised_bldg_area'] = revised_bldg_area
            item['n2021_land_val'] = n2021_land_val
            item['n2021_bldg_val'] = n2021_bldg_val
            item['n2021_total_val'] = n2021_total_val
            item['n2021_assd_land_val'] = n2021_assd_land_val
            item['n2021_assd_bldg_val'] = n2021_assd_bldg_val
            item['n2021_total_assd_val'] = n2021_total_assd_val
            item['n2021_hmsd_ex_val'] = n2021_hmsd_ex_val
            item['n2021_tax_assmt'] = n2021_tax_assmt
            item['n2020_land_val'] = n2020_land_val
            item['n2020_bldg_val'] = n2020_bldg_val
            item['n2020_total_val'] = n2020_total_val
            item['n2020_assd_land_val'] = n2020_assd_land_val
            item['n2020_assd_bldg_val'] = n2020_assd_bldg_val
            item['n2020_total_assd_val'] = n2020_total_assd_val
            item['n2020_hmsd_ex_val'] = n2020_hmsd_ex_val
            item['n2020_tax_assmt'] = n2020_tax_assmt
            item['n2019_land_val'] = n2019_land_val
            item['n2019_bldg_val'] = n2019_bldg_val
            item['n2019_total_val'] = n2019_total_val
            item['n2019_assd_land_val'] = n2019_assd_land_val
            item['n2019_assd_bldg_val'] = n2019_assd_bldg_val
            item['n2019_total_assd_val'] = n2019_total_assd_val
            item['n2019_hmsd_ex_val'] = n2019_hmsd_ex_val
            item['n2019_tax_assmt'] = n2019_tax_assmt

            yield item