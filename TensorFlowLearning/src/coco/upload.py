# %matplotlib inline
import sys

from pycocotools.coco import COCO
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

from obs import ObsClient


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

  catIds = [10];
  imgIds = coco.getImgIds(catIds=catIds);
  print(imgIds.__len__())

  access_key = argv[1]
  secret_key = argv[2]
  end_point = argv[3]
  obs_client = ObsClient(
    access_key_id=access_key,
    secret_access_key=secret_key,
    server=end_point,
    long_conn_mode=True
  )

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

  imgIdsList = []
  for i in range(imgIds.__len__()):
    imgIdsList.append(imgIds[i])

  imgs = coco.loadImgs(imgIdsList)
  for i in range(imgIds.__len__()):
    img = imgs[i]
    print(i, end="\t")
    print(img['file_name']);

    path = "s3://modelartscarbon/traffic-light-input/" + img['file_name']

    bucket_name, file = parser_path(path)

    resp = obs_client.putFile(bucket_name, file,
                              file_path="/Users/xubo/Desktop/xubo/data/train2017/" + img['file_name'])

    if resp.status < 300:
      print('requestId:', resp.requestId)
    else:
      print('errorCode:', resp.errorCode)
      print('errorMessage:', resp.errorMessage)

  print(i)

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
  # If user want to test OBS, please input ak, sk and endpoint.
  main(sys.argv)
  print("Success")
