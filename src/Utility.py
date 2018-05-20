def slice(img):
    slicesX = 20
    slicesY = 20

    left = 259 + 2

    #constants that in future should be generated automatically by detecting edges and calculating
    slice_sizeX = 48
    slice_sizeY = 48
    plusMovementX = 2
    plusMovementY = 2

    countX = 1

    list_to_be_returned = []

    for X in range(slicesX):
        right = left + slice_sizeX

        temp_list = []

        upper = 30 + 2
        countY = 1
        for Y in range(slicesY):
            lower = upper + slice_sizeY

            equalizer = 2
            bbox = (left+equalizer, upper+equalizer, right+equalizer, lower+equalizer)
            working_slice = img.crop(bbox)
            upper += slice_sizeY + plusMovementY

            temp_list.append(working_slice)

            countY += 1

        left += slice_sizeX  + plusMovementX
        countX += 1
        list_to_be_returned.append(temp_list)
    return list_to_be_returned