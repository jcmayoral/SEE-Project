clear a;
a = webcam(1);
baseString = '/home/jose/Dropbox/MAS/Semester3/SEE/Assignment/03/images/measurement';
extension = '.jpg';
n = 21;

while(n < 40)
    preview(a);
    pause()
    newImage = snapshot(a);
    imwrite(newImage,strcat(baseString, int2str(n),extension));
    n = n+1;
end

