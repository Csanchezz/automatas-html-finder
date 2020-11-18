import re 


def get_html(new_str, info_back=True):
    return_obj = {}

    # test_str = '<table class="table-bootstrap" name="tablename">Here will be the table</table> <a href="www.google.com" width="90px"> photo </a>'
    # print("The original string is : " + str(new_str)) 
    reg_str_v1 = '<(?![\/]).*?>*<.*?>'
    
    reg_str_v2 = '<(?![\/]).*?>.*?'


    if info_back:
        tags = re.findall(reg_str_v1, new_str) 
    else: 
        tags = re.findall(reg_str_v2, new_str) 

    

    # print("The TAGS extracted : " + str(tags)) 

    tags_info = []

    for tag in tags:
        new_tag_regex = "<(?![\/])(\w+)"
        new_tag = re.findall(new_tag_regex, tag)
        newtagname = '{}'.format(new_tag[0])
        
        objet_to_insert = {'name': newtagname}

        
        if info_back: 
            info_reg_v1 = '<(?![\/]).*?>(.*?)<'
            info = re.findall(info_reg_v1, tag)
            objet_to_insert['info'] = info[0]
        else: 
            reg_subs_v1 = '(\w+)=' # this for atts
            attrs = re.findall(reg_subs_v1, tag)
            obj_attrs = []

            for attr in attrs:
                reg_subs_v2 = '{}="{}"'.format(attr, "(.*?)")   # this for atts
                value = re.findall(reg_subs_v2, tag)
                value_str = "{}={}".format(attr, value[0])

                obj_attrs.append(value_str)

                # print(value_str)
            objet_to_insert['attrs'] = obj_attrs
        

        # print("this is the info  for tag {} : {}".format(tag, info))
        # print("THE ATTRS EXTRACTED for {} are {}".format( tag , attrs))    




        # return_obj[newtagname] = {'info': info[0]} 

        

        tags_info.append(objet_to_insert)

        # return_obj[newtagname]['attrs'] = obj_attrs
    
    # return_obj['tags'] = tags
    return_obj['tags_info'] = tags_info

    return return_obj