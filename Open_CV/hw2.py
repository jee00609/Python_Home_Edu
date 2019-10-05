import cv2 as cv
import numpy as np

#흰색 그림 넣기
img = cv.imread('img/blank_500.jpg')

#Lines 글 추가
cv.putText(img,"Lines",(30,40),cv.FONT_HERSHEY_PLAIN,1,(0,0,0))

#줄 긋기 순서대로 파 초 빨
cv.line(img,(50,50),(150,50),(255,0,0))
cv.line(img,(200,50),(300,50),(0,255,0))
cv.line(img,(350,50),(450,50),(0,0,255))

# Rectangle 글 추가
cv.putText(img,"Rectangle",(30,80),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255))

#사각형 긋기 순서대로 파 초 빨
cv.rectangle(img,(90,90),(150,150),(255,0,0))
cv.rectangle(img,(230,90),(290,150),(0,255,0),10)
cv.rectangle(img,(370,90),(430,150),(0,0,255),-1)

# Polyline 글 추가
cv.putText(img,"Polyline",(30,180),cv.FONT_HERSHEY_PLAIN,1,(0,255,255))

#번개모양 / 3각형 열린선 / 3각형 닫힌도형 /5각형 닫힌 도형
pts1=np.array([[50,190],[90,250],[60,220],[110,290]],dtype=np.int32)
cv.polylines(img,[pts1],False,(255,0,0))

pts2=np.array([[180,200],[150,280],[230,280]],dtype=np.int32)
cv.polylines(img,[pts2],False,(0,0,0),10)

pts3=np.array([[280,200],[250,280],[330,280]],dtype=np.int32)
cv.polylines(img,[pts3],True,(0,0,255),10)

pts4=np.array([[410,200],[360,240],[390,290],[430,290],[460,240]],dtype=np.int32)
cv.polylines(img,[pts4],True,(0,0,0))

# Circle 글 추가
cv.putText(img,"Circle",(30,300),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,0,0))

#원점/ 반지름/ 회전0/ 0도부터360도
cv.ellipse(img,(50,360),(50,50),0,0,360,(255,0,0))
#원점/ 아래반원 그리기
cv.ellipse(img,(150,360),(50,50),0,0,180,(255,0,0))
#원점/ 위반원 그리기
cv.ellipse(img,(200,360),(50,50),0,181,360,(0,0,255))

#원점/ 반지름 납작한 타원 그리기
cv.ellipse(img,(325,360),(75,50),0,0,360,(0,255,0))
#원점/ 반지름 홀쭉한 타원 그리기
cv.ellipse(img,(450,360),(50,75),0,0,360,(255,0,255))

#원점/반지름 40/ 두께5
cv.circle(img,(50,420),40,(0,255,0),5)
#원점/반지름 20/ 채우기
cv.circle(img,(50,460),20,(0,0,255),-1)


#원점/ 반지름/회전 15도
cv.ellipse(img,(180,450),(25,55),40,0,360,(0,0,0))

#원점/ 홀쭉한 타원 45도 회전 후 아래 반원 그리기
cv.ellipse(img,(300,450),(25,55),40,0,180,(0,0,255))

#원점/ 홀쭉한 타원 45도 회전 후 위 반원 그리기
cv.ellipse(img,(350,450),(25,55),40,181,360,(255,0,0))


cv.imshow('np-image',img) #이거 실행되다가 에러남
cv.waitKey(0)#따라서 이걸 추가해야함
cv.destroyAllWindows()#내가 아무 키를 누르는 순간 창을 닫음