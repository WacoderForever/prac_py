
def imresize(im,sz):
    pil_im = Image.fromarray(im)    

    return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
    imhist,bins = histogram(im.flatten,nbr_bins,density=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf /cdf[-1]

    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape),cdf

def compute_average(img_list):
    average_im = array(Image.open(img_list[0]),'f')

    for imname in img_list[1:]:
        try:
            average_im += array(Image.open(imname))
        except:
            print(f"{imname}.......skipped")
    average_im /= len(img_list) 

    return array(average_im,"uint8")
