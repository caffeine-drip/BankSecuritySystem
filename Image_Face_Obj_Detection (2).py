import httplib, urllib, base64, json
import cv2, time, thread
iters = 0
# https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/image?iterationId=0601e978-1575-4410-bf4d-31f27fa0de26
cap = cv2.VideoCapture(1)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.


# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
text1 = ['Unknown']*10
text2 = ['No object Detected']
headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Prediction-key': '5efccca2a1bb44f599428c8ab4b2c01f',
}
params = urllib.urlencode({
    # Request parameters
    'application': 'OverWatch',
})

def calling_api(img,kk,ori):
    global text1,text2,iters
    conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v1.0/Prediction/c6da9a55-b5f4-40e2-b2e2-7bb1d21e5309/image?%s" % params, img.read(), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    parsed = json.loads(data)
    #print(parsed)
    conn.close()
    texting = parsed['Predictions'][0]['Tag']
    conf = parsed['Predictions'][0]['Probability']
    if conf> 0.85:
        path = '//home//arpit//opencv_prog//detected_images//'+str(str(iters)+'#'+time.strftime("%d-%m-%Y")+' '+texting)
        #print(path)
        path+='.jpg'
        cv2.imwrite(path, ori)
        iters+=1
    if texting in ['Gun']:
        text2[0] = texting
        
        
        
        if conf > 0.02:
            text2[0] += 'Detected'
    else:
        text1[kk] = texting
        text1[kk] += ' Confidence : '
        
        
        if conf > 0.5:
            
            
            text1[kk] += str('%.2f'% conf)
        else:
            text1[kk] = 'Unknown'
        text2[0] = 'No object Detected'
def calling_api2(img,kk,ori):
    global text1,text2,iters
    conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v1.0/Prediction/c6da9a55-b5f4-40e2-b2e2-7bb1d21e5309/image?%s" % params, img.read(), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    parsed = json.loads(data)
    #print(parsed)
    conn.close()
    texting = parsed['Predictions'][0]['Tag']
    conf = parsed['Predictions'][0]['Probability']
    
    if texting in ['Gun']:
        text2[0] = texting
        
        
        
        if conf > 0.02:
            text2[0] += 'Detected'
    else:
        text1[kk] = texting
        text1[kk] += ' Confidence : '
        
        
        if conf > 0.5:
            
            
            text1[kk] += str('%.2f'% conf)
        else:
            text1[kk] = 'Unknown'
        text2[0] = 'No object Detected'

    
# The URL of a JPEG image to analyze.
i=0
j=0
while True:
    ret, img = cap.read()
    
    # cv2.waitKey(0)
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 7)
    for kk,(x,y,w,h) in enumerate(faces):
        #print(w*h)
        #if w*h > 6500:
        # img_sv = img[y-10:y+h+10, x-10:x+w+10]
        img_sv = img
        cv2.imwrite('x.jpg', img_sv)
        img1 = open('x.jpg', 'rb')

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(img, text1[kk] ,(x, y-20), font, .5,(255,255,255),2,cv2.CV_AA)
        if i%25 == 0:
            thread.start_new_thread(calling_api2, (img1,kk,img_sv) )
        cv2.imshow('Image',img)
    cv2.imwrite('xx.jpeg', img)
    # cv2.waitKey(0)
    img2 = open('xx.jpeg','rb')
    if i%25 == 0:
        thread.start_new_thread(calling_api, (img2,0,img) )
    cv2.putText(img, text2[0] ,(20, 20), font, .5,(255,255,255),2,cv2.CV_AA)
    if i>100:
        i = i%50
    j+=1

    
    
    openn = True
    

    
    
    
        #print(parsed)
        # text = parsed['categories']
        # print(text[0])
        # if text ==[]:
        #     text = 'Unknown'
        # else:
        #     text = text[0]['name']
        # # print(text)
        # conn.close()
    
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    i+=1
    
    # time.sleep(2)vb
cap.release()
cv2.destroyAllWindows()
    
