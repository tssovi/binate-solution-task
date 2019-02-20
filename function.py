import urllib.request
import re


def GetImage(url, img_path, img_name):
    '''
      This function take url and image url as input. If the url is valid then it save the in local disk and generate
      true response if the url is invalid then it generate false response. Then return the response to ReadFile()
      function for further action.
    '''
    try:
        urllib.request.urlretrieve(url, img_path+img_name)
        return True
    except:
        return False


def ReadFile(file_path, img_path):
    '''
      This function take file path as input and extract urls from file. Then in a for loop it request GetImage()
      function to download the image that contains in url. Then it grab returned response and print feedback against
      that response.
    '''
    with open(file_path, "r") as urls:
        url_dict = {'valid': 0, 'invalid': 0}
        for url in urls:
            # Split the url
            temp_img_name = re.sub(r'\s', '', url).split('/')
            # Pick last part of the url as image name
            img_name = temp_img_name[3] + '.jpeg'

            flag = GetImage(url, img_path, img_name)
            if flag:
                print(img_name, 'This image downloaded successfully in {} folder.'.format(img_path))
                url_dict['valid'] = url_dict['valid'] + 1
            else:
                print('Error!!! Image download failed. {} This url is invalid.'.format(url.rstrip()))
                url_dict['invalid'] = url_dict['invalid'] + 1
        return url_dict
