import os

def func():
    for i in range(len(os.listdir(path_dir))):
        f = open(path_dir + '\\' + os.listdir(path_dir)[i], 'rb')

        sigHead1 = f.read(4)
        f.seek(2, 1)
        sigHead2 = (f.read(2))
        f.seek(-2, 2)
        sigFoot = f.read(2)

        if sigHead1 == b'\xff\xd8\xff\xe0' and sigHead2 == b'JF' and sigFoot == b'\xff\xd9':
            isJPEG.append(os.listdir(path_dir)[i])
        f.close()

    for j in range(len(isJPEG)):
        os.rename(path_dir + '\\' + isJPEG[j], path_dir + '\\' + isJPEG[j] + '.jpeg')

if __name__ == '__main__':

    path_dir = 'C:\\Users\82107\OneDrive - 서울여자대학교\BoB 10th\\04. Assignment Stack\\09 OSDF-3 [강정윤] 과제제출\File_Signature_Examples'
    sigHead_JPEG = b'\xff\xd8\xff\xe0'
    sigFoot_JPEG = b'\xff\xd9'
    isJPEG = []

    func()