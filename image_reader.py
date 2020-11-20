import numpy as np
import cv2
import os
os.chdir(r"C:\Users\dell\Desktop\ATMobile2020-1\pics")

def getCornerHarris(srcImg):
    grayImg = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", grayImg)
    chImg = cv2.cornerHarris(grayImg, 10, 5, 0.01)

    rstChImg = srcImg.copy()
    rstChImg[chImg > 0.01 * chImg.max()] = [0, 255, 0]
    return rstChImg

def getSiftKeyPoints(srcImg):
    grayImg = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptor = sift.detectAndCompute(grayImg, None)
    siftImg = srcImg.copy()
    siftImg = cv2.drawKeypoints(srcImg, keypoints = keypoints, outImage = siftImg, flags = cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    return siftImg

def getSurfKeyPoints(srcImg):
    grayImg = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
    surf = cv2.xfeatures2d.SURF_create(4000)
    keypoints, descriptor = surf.detectAndCompute(grayImg, None)
    surfImg = srcImg.copy()
    surfImg = cv2.drawKeypoints(srcImg, keypoints = keypoints, outImage = surfImg, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    return surfImg

def getOrbKeyPoints(srcImg):
    grayImg = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    kpSrc, desSrc = orb.detectAndCompute(grayImg, None)
    orbImg = srcImg.copy()
    orbImg = cv2.drawKeypoints(srcImg, keypoints=kpSrc, outImage=orbImg, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    return orbImg

def getStarKeyPoints(srcImg):
    grayImg = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)

    # keypoints, descriptor = sift.detectAndCompute(pic2, None)
    star = cv2.xfeatures2d.StarDetector_create()
    kpStar = star.detect(grayImg)
    starImg = srcImg.copy()
    starImg = cv2.drawKeypoints(srcImg, keypoints=kpStar, outImage=starImg, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    cv2.imshow("Star", starImg)

    sift = cv2.xfeatures2d.SIFT_create()
    kpSift, features = sift.compute(grayImg, kpStar)

    starImg = srcImg.copy()
    starImg = cv2.drawKeypoints(srcImg, keypoints=kpSift, outImage=starImg, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    return starImg

# 对加载的每个图片进行特征提取并展示
def showOnePicKeyPoints(pImg):
    srcImg = cv2.imread(pImg)
    cv2.imshow("Src Img", srcImg)

    chImg = getCornerHarris(srcImg)
    cv2.imshow("CornerHarris", chImg)

    siftImg = getSiftKeyPoints(srcImg)
    cv2.imshow("Sift", siftImg)

    surfImg = getSurfKeyPoints(srcImg)
    cv2.imshow("Surf", surfImg)

    orbImg = getOrbKeyPoints(srcImg)
    cv2.imshow("Orb", orbImg)

    starImg = getStarKeyPoints(srcImg)
    cv2.imshow("Star-sift", starImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 加载所有图片
filedir = r"C:\Users\dell\Desktop\ATMobile2020-1\pics"
filenames = os.listdir(filedir)
for root, dirs, files in os.walk("./pics"):
    for name in files:
        print(os.path.join(root, name))
        pImg = os.path.join(root, name)
        showOnePicKeyPoints(pImg=pImg)

pics = r"C:\Users\dell\Desktop\ATMobile2020-1\pics"
for pic in os.listdir(pics):
    showOnePicKeyPoints(pic)