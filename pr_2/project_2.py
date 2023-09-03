import pyAesCrypt

password = input('Введите пароль: ')

# для шифровки файла
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#для расшифровки
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
#124351
