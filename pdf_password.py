import pikepdf

old_pdf = pikepdf.Pdf.open("sample_pdf.pdf")

#object to stop the permission for accessing
no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("pro_new.pdf",
             encryption=pikepdf.Encryption(user="123asd",
                                           owner="wscube",
                                           allow=no_extr))






