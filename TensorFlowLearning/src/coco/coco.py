# %matplotlib inline
import sys

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

from obs import ObsClient, AppendObjectContent


def main(argv):
  pylab.rcParams['figure.figsize'] = (8.0, 10.0)

  dataDir = '/Users/xubo/Downloads'
  dataType = 'train2017'
  annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataType)

  # initialize COCO api for instance annotations
  coco = COCO(annFile)

  # display COCO categories and supercategories
  cats = coco.loadCats(coco.getCatIds())
  nms = [cat['name'] for cat in cats]
  print('COCO categories: \n{}\n'.format(' '.join(nms)))

  nms = set([cat['supercategory'] for cat in cats])
  print('COCO supercategories: \n{}'.format(' '.join(nms)))

  # get all images containing given categories, select one at random
  # sum = 0
  # for num in range(70):
  #   catIds = [num];
  #   imgIds = coco.getImgIds(catIds=catIds);
  #   print(str(num) + ":" + str(imgIds.__len__()))
  #   sum = sum + imgIds.__len__()
  # print(sum)

  catIds = [10];
  imgIds = coco.getImgIds(catIds=catIds);
  print(imgIds.__len__())
  # for i in range(1):

  access_key = argv[1]
  secret_key = argv[2]
  end_point = argv[3]
  obs_client = ObsClient(
    access_key_id=access_key,
    secret_access_key=secret_key,
    server=end_point,
    long_conn_mode=True
  )

  s3 = "s3:"
  prefix_s3 = "s3://"
  prefix_s3_upper = "S3://"
  separator = "/"

  def parser_path(path):
    """
    parser the path and return bucket_name and file_name
    """
    base_url = str(path)[len(prefix_s3):] or str(path)[len(prefix_s3_upper):]
    split_array = base_url.split(separator)
    bucket_name = split_array[0]
    file_name = separator.join(split_array[1:])
    return bucket_name, file_name

  for i in range(imgIds.__len__()):
    # im=np.random.randint(0, len(imgIds))
    # print(im)
    # img = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[i]
    img = coco.loadImgs(imgIds[i])[0]
    print(i, end="\t")
    print(img['file_name']);
    url = img['coco_url']
    import requests
    r = requests.get(url)

    path = "s3://carbonsouth/trafficlight/" + img['file_name']
    path2 = "s3://carbonsouth/trafficlight/a" + img['file_name']
    path3 = "s3://carbonsouth/trafficlight/b" + img['file_name']

    bucket_name, file = parser_path(path)
    bucket_name2, file2 = parser_path(path2)
    bucket_name3, file3 = parser_path(path3)

    content = AppendObjectContent()
    # for line in manifest_json:
    #   content.content = line + "\n"
    content.content = r.content
    resp = obs_client.appendObject(bucket_name, file, content=content)
    content.position = resp.body.nextPosition

    resp = obs_client.appendObject(bucket_name2, file2, content=content)
    content.position = resp.body.nextPosition

    resp = obs_client.appendObject(bucket_name3, file3, content=content)
    content.position = resp.body.nextPosition
    # return resp.body.buffer

  print(i)

  # bucket_name, file = parser_path(path)
  # content = AppendObjectContent()
  # for line in manifest_json:
  #   content.content = line + "\n"
  #   resp = obs_client.appendObject(bucket_name, file, content=content)
  #   content.position = resp.body.nextPosition
  # return resp.body.buffer

  # load and display image
  # I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
  # use url to load image
  I = io.imread(img['coco_url'])
  plt.axis('off')
  plt.imshow(I)
  plt.show()

  # load and display instance annotations
  plt.imshow(I);
  plt.axis('off')
  annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
  anns = coco.loadAnns(annIds)
  coco.showAnns(anns)


if __name__ == '__main__':
  # If user want to test OBS, please input OBS path, ak, sk and endpoint.
  main(sys.argv)
  print("Success")
