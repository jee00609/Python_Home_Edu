import cv2 as cv
import numpy as np

#��� �׸� �ֱ�
img = cv.imread('img/blank_500.jpg')

#Lines �� �߰�
cv.putText(img,"Lines",(30,40),cv.FONT_HERSHEY_PLAIN,1,(0,0,0))

#�� �߱� ������� �� �� ��
cv.line(img,(50,50),(150,50),(255,0,0))
cv.line(img,(200,50),(300,50),(0,255,0))
cv.line(img,(350,50),(450,50),(0,0,255))

# Rectangle �� �߰�
cv.putText(img,"Rectangle",(30,80),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255))

#�簢�� �߱� ������� �� �� ��
cv.rectangle(img,(90,90),(150,150),(255,0,0))
cv.rectangle(img,(230,90),(290,150),(0,255,0),10)
cv.rectangle(img,(370,90),(430,150),(0,0,255),-1)

# Polyline �� �߰�
cv.putText(img,"Polyline",(30,180),cv.FONT_HERSHEY_PLAIN,1,(0,255,255))

#������� / 3���� ������ / 3���� �������� /5���� ���� ����
pts1=np.array([[50,190],[90,250],[60,220],[110,290]],dtype=np.int32)
cv.polylines(img,[pts1],False,(255,0,0))

pts2=np.array([[180,200],[150,280],[230,280]],dtype=np.int32)
cv.polylines(img,[pts2],False,(0,0,0),10)

pts3=np.array([[280,200],[250,280],[330,280]],dtype=np.int32)
cv.polylines(img,[pts3],True,(0,0,255),10)

pts4=np.array([[410,200],[360,240],[390,290],[430,290],[460,240]],dtype=np.int32)
cv.polylines(img,[pts4],True,(0,0,0))

# Circle �� �߰�
cv.putText(img,"Circle",(30,300),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,0,0))

#����/ ������/ ȸ��0/ 0������360��
cv.ellipse(img,(50,360),(50,50),0,0,360,(255,0,0))
#����/ �Ʒ��ݿ� �׸���
cv.ellipse(img,(150,360),(50,50),0,0,180,(255,0,0))
#����/ ���ݿ� �׸���
cv.ellipse(img,(200,360),(50,50),0,181,360,(0,0,255))

#����/ ������ ������ Ÿ�� �׸���
cv.ellipse(img,(325,360),(75,50),0,0,360,(0,255,0))
#����/ ������ Ȧ���� Ÿ�� �׸���
cv.ellipse(img,(450,360),(50,75),0,0,360,(255,0,255))

#����/������ 40/ �β�5
cv.circle(img,(50,420),40,(0,255,0),5)
#����/������ 20/ ä���
cv.circle(img,(50,460),20,(0,0,255),-1)


#����/ ������/ȸ�� 15��
cv.ellipse(img,(180,450),(25,55),40,0,360,(0,0,0))

#����/ Ȧ���� Ÿ�� 45�� ȸ�� �� �Ʒ� �ݿ� �׸���
cv.ellipse(img,(300,450),(25,55),40,0,180,(0,0,255))

#����/ Ȧ���� Ÿ�� 45�� ȸ�� �� �� �ݿ� �׸���
cv.ellipse(img,(350,450),(25,55),40,181,360,(255,0,0))


cv.imshow('np-image',img) #�̰� ����Ǵٰ� ������
cv.waitKey(0)#���� �̰� �߰��ؾ���
cv.destroyAllWindows()#���� �ƹ� Ű�� ������ ���� â�� ����