import pandas



b2b = pandas.read_csv('#B2B MASTER __ AUTO-CALCULATION - Biomondi.csv')




#b2b code

pos = []
for key,  column in b2b.to_dict()['Pos'].items():
    pos.append(column)

sku = []
for key,  column in b2b.to_dict()['SKU'].items():
    sku.append(column)

product_description = []
for key,  column in b2b.to_dict()['Product Description'].items():
    product_description.append(column)

menge_unit_ref = []
for key,  column in b2b.to_dict()['Menge / Unit (Reference)'].items():
    menge_unit_ref.append(column)

product_quant = []
for key,  column in b2b.to_dict()['Product Qty'].items():
    product_quant.append(column)

purchase = []
for key,  column in b2b.to_dict()['Purchase'].items():
    purchase.append(column)

shipping = []
for key,  column in b2b.to_dict()['Shipping'].items():
    shipping.append(column)

free_shipping = []
for key,  column in b2b.to_dict()['Free Shipping'].items():
    free_shipping.append(column)

purchace_incl_freight = []
for key,  column in b2b.to_dict()['Purchace incl. Freight'].items():
    purchace_incl_freight.append(column)

purchasing_total = []
for key,  column in b2b.to_dict()['Purchasing Total'].items():
    purchasing_total.append(column)

margin_per = []
for key,  column in b2b.to_dict()['Margin %'].items():
    margin_per.append(column)

yield_ = []
for key,  column in b2b.to_dict()['Yield'].items():
    yield_.append(column)

unique_selling_price = []
for key,  column in b2b.to_dict()['Unique Selling Price'].items():
    unique_selling_price.append(column)

total_selling_price = []
for key,  column in b2b.to_dict()['Total Selling Price'].items():
    total_selling_price.append(column)

final_pos = []
temp_list = []
# nan = False
result = []
for i in pos:
    nan = False
    if str(i) != 'nan':
        temp_list.append(i)
        # print(temp_list)
        result.append(temp_list)
        temp_list = []
        # nan = True
        # pass
    else:
        temp_list.append(i)
        # nan = True
result.append(temp_list)

# print(result)

# print(result)
for item in range(len(result)):
    # try:
    try:
        las = result[item].pop()
        result[item+1].insert(0, las)
    except:
        print('emp')
result[-1].append(None)
pos_numbers = result[1:]
# print(pos_numbers)
item_len_num = []
for te in pos_numbers:
    item_len_num.append(len(te))
    # print(last_item)
# print(len(item_len_num))

final_b2bs = {}
start_num = 0

for item in range(len(item_len_num)):
    # print(sku[start_num])
    finalpos = ''
    for it in pos[start_num: start_num+item_len_num[item]]:
        print(it)
        if str(it) != 'nan':
            finalpos += f'{it} '
    print(finalpos)
    final_skus = ''
    for it in sku[start_num: start_num+item_len_num[item]]:
        if str(it) != 'nan':
            final_skus += f'{it} '

    final_pro_des = ''
    for it in product_description[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_pro_des += f'{it} '

    final_menge = ''
    for it in menge_unit_ref[start_num: start_num+item_len_num[item]]:
        if str(it) != 'nan':
            final_menge += f'{it} '

    final_purchase = ''
    for it in purchase[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_purchase += f'{it} '

    final_shipping = ''
    for it in shipping[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_shipping += f'{it} '

    final_free_shipping = ''
    for it in free_shipping[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_free_shipping += f'{it} '

    final_purchase_incl_freight = ''
    for it in purchace_incl_freight[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_purchase_incl_freight += f'{it} '

    final_purchasing_total = ''
    for it in purchasing_total[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_purchasing_total += f'{it} '

    final_margin_per = ''
    for it in margin_per[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':

            final_margin_per += f'{it} '

    final_yield = ''
    for it in yield_[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':

            final_yield += f'{it} '
    # final_pro_quant
    # for
    # final_total_selling_check = total_selling_price[start_num: start_num + item_len_num[item]]
    final_pro_quant = product_quant[start_num: start_num + item_len_num[item]]
    final_unique_selling = unique_selling_price[start_num: start_num + item_len_num[item]]
    final_quan_price_ratio = ''
    for it in range(len(final_unique_selling)):
        if str(final_unique_selling[it]) != 'nan':
            do = final_unique_selling[it].replace('€', '').replace(',', '.')
            if str(final_pro_quant[it]).split('.')[-1] == "0":
                final_quan_price_ratio += f"{int(final_pro_quant[it])}:{do},"
            elif str(final_pro_quant[it]).split('.')[-1] != "0":
                final_quan_price_ratio += f"{int(str(final_pro_quant[it]).replace('.', ''))}:{do},"
                print('here __', str(final_pro_quant[it]))#.replace('.', ''))
    # if final_quan_price_ratio[-1]
    final_total_selling = ''
    for it in purchasing_total[start_num: start_num + item_len_num[item]]:
        if str(it) != 'nan':
            final_total_selling += f'{it.replace(",", ".")} '
            break
    # print(final_quan_price_ratio)
    # print('fFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf',final_total_selling)
    try:
        final_quan_price_temp = ''
        # for it in range(len([]):
        if '-pal' not in final_skus.lower() and float(final_total_selling.strip()) > 300:
            for val in final_quan_price_ratio.split(','):
                print('=======================================================================================iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', final_skus)
                unified_tas = val.split(':')
                # print(val)

                # print(unified_tas)
                if len(str(int(float(unified_tas[0])/2))) > 2 and str(int(float(unified_tas[0])/2))[-1] != "0":
                    final_quan_price_temp += f'{int(int(float(unified_tas[0])/2)/10)*10}:{unified_tas[1]}, '
                else:
                    final_quan_price_temp += f'{int(float(unified_tas[0]) / 2)}:{unified_tas[1]}, '

            # break
            # print(final_quan_price_temp)

        elif '-pal' in final_skus.lower() and float(final_total_selling.strip()) > 4000:
            # final_quan_price_ratio = ''
            for val in final_quan_price_ratio.split(','):
                print('========================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', final_skus)
                unified_tas = val.split(':')
                print(val)
                # print(unified_tas)
                if len(str(int(float(unified_tas[0])/2))) > 2 and str(int(float(unified_tas[0])/2))[-1] != "0":
                    final_quan_price_temp += f'{int(int(float(unified_tas[0])/2)/10)*10}:{unified_tas[1]}, '
                else:
                    final_quan_price_temp += f'{int(float(unified_tas[0]) / 2)}:{unified_tas[1]}, '
                print(final_quan_price_temp)
        else:
            print("COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEECTTTTTT", final_skus)

        if '-pal' not in final_skus.lower() and float(final_total_selling.strip()) < 100:
            for val in final_quan_price_ratio.split(','):
                print('=======================================================================================iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', final_skus)
                unified_tas = val.split(':')
                # print(val)

                # print(unified_tas)
                if len(str(int(float(unified_tas[0])*1.50))) > 2 and str(int(float(unified_tas[0])*1.50))[-1] != "0":
                    final_quan_price_temp += f'{int(int(float(unified_tas[0])*1.5)/10)*10}:{unified_tas[1]}, '
                else:
                    final_quan_price_temp += f'{int(float(unified_tas[0])*1.5)}:{unified_tas[1]}, '

            # print("happy sing",final_quan_price_temp)# * float(final_quan_price_temp.split(",")[0].split(':')[1]))
            # if '-pal' not in final_skus.lower() and float(final_quan_price_temp.split(",")[0].split(':')[0]) * float(final_quan_price_temp.split(",")[0].split(':')[1]) < 100:
            #     final_quan_price_tem = final_quan_price_temp
            #     final_quan_price_temp = ''
            #     for val in final_quan_price_tem.split(','):
            #         print('))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',final_skus)
            #         unified_tas = val.split(':')
            #         # print(val)
            #
            #         # print(unified_tas)
            #         if len(str(int(float(unified_tas[0]) / 2))) > 2 and str(int(float(unified_tas[0]) / 2))[-1] != "0":
            #             final_quan_price_temp += f'{int(int(float(unified_tas[0]) * 1.25) / 10) * 10}:{unified_tas[1]}, '
            #         else:
            #             final_quan_price_temp += f'{int(float(unified_tas[0]) * 1.25)}:{unified_tas[1]}, '

                    # print(final_quan_price_temp)

                    # final_quan_price_temp += f'{int(float(unified_tas[0])/2)}:{unified_tas[1]}, '
            # print(final_quan_price_ratio)
            # if '-pal' not in final_skus[it] and float(final_total_selling.strip()) <100:
            #     print(final_total_selling.strip(),
            #           '----------------------------------------------------------------------------------------------------------------------------------------------------')
            #
            #     # final_quan_price_ratio = ''
            #     for val in final_quan_price_ratio.split(','):
            #         unified_tas = val.split(':')
            #
            #         # print(unified_tas)
            #         if len(str(int(float(unified_tas[0])*1.25))) > 2 and str(int(float(unified_tas[0])*1.25))[-1] != "0":
            #             final_quan_price_temp += f'{int(int(float(unified_tas[0])*1.25)/10)*10}:{unified_tas[1]}, '
            #         # final_quan_price_temp += f'{int(float(unified_tas[0])/2)}:{unified_tas[1]}, '
            # if '-pal' not in final_skus[it] and float(final_total_selling.strip()) <100:
            #     # final_quan_price_ratio = ''
            #     for val in final_quan_price_ratio.split(','):
            #         unified_tas = val.split(':')
            #
            #         # print(unified_tas)
            #         if len(str(int(float(unified_tas[0])*1.25))) > 2 and str(int(float(unified_tas[0])*1.25))[-1] != "0":
            #             final_quan_price_temp += f'{int(int(float(unified_tas[0])*1.25)/10)*10}:{unified_tas[1]}, '
            #         # final_quan_price_temp += f'{int(float(unified_tas[0])/2)}:{unified_tas[1]}, '
            # if '-pal' not in final_skus[it] and float(final_total_selling.strip()) <100:
            #     # final_quan_price_ratio = ''
            #     for val in final_quan_price_ratio.split(','):
            #         unified_tas = val.split(':')
            #
            #         # print(unified_tas)
            #         if len(str(int(float(unified_tas[0])*1.25))) > 2 and str(int(float(unified_tas[0])*1.25))[-1] != "0":
            #             final_quan_price_temp += f'{int(int(float(unified_tas[0])*1.25)/10)*10}:{unified_tas[1]}, '
            #         # final_quan_price_temp += f'{int(float(unified_tas[0])/2)}:{unified_tas[1]}, '
        # print(float(final_total_selling.strip()), '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        # print(final_quan_price_temp, 'happu')
    except Exception as ex:
        print(ex)
    try:
        print('harsh', float(final_quan_price_temp.split(",")[0].split(':')[0]) * float(final_quan_price_temp.split(",")[0].split(':')[1]) <100)
        if final_quan_price_temp != '' and '-pal' not in final_skus.lower() and float(final_quan_price_temp.split(",")[0].split(':')[0]) * float(final_quan_price_temp.split(",")[0].split(':')[1]) < 100:
                final_quan_price_tem = final_quan_price_temp
                final_quan_price_temp = ''
                for val in final_quan_price_tem.split(','):
                    print('))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',final_skus)
                    unified_tas = val.split(':')
                    # print(val)
                    # print(unified_tas)
                    if len(str(int(float(unified_tas[0]) / 2))) > 2 and str(int(float(unified_tas[0]) / 2))[-1] != "0":
                        final_quan_price_temp += f'{int(int(float(unified_tas[0]) * 1.25) / 10) * 10}:{unified_tas[1]}, '
                    else:
                        final_quan_price_temp += f'{int(float(unified_tas[0]) * 1.25)}:{unified_tas[1]}, '

                print(final_skus, 'lessu')
    except:
        print('more than 100')




    if '' == str(final_quan_price_temp):
        print('haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaai')
        final_quan_price_ratio = final_quan_price_ratio[:-1]

        pass
    else:
        print('Naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahi', final_quan_price_temp)
        final_quan_price_ratio = final_quan_price_temp
        final_quan_price_ratio = final_quan_price_ratio[:-2]

        # print('yes nan in usa')
        # final_quan_price_ratio = final_quan_price_ratio
        # else:
        #     final_quan_price_ratio =
    final_b2bs[sku[start_num]] = {'POS': [finalpos],
                                  'SKU': [final_skus],
                                  'Quantity And Unique Selling Ratio': [final_quan_price_ratio],
                                 'Product Description': [final_pro_des],
                                 'Menge / Unit (Reference)': [final_menge],
                                 'Purchase': [final_purchase],
                                   'Shipping': [final_shipping],
                                  'Free Shipping': [final_free_shipping],
                                  'Purchace incl. Freight': [final_purchase_incl_freight],
                                  'Purchasing Total': [final_purchasing_total],
                                  'Margin %': [final_margin_per],
                                  'Yield': [final_yield],
                                  'Total Selling Price': [final_total_selling],
                                  'Max len': 0
                                  }

    start_num += item_len_num[item]

# for key, item in final_b2bs.items():
#     print(key)
#     if '100556010000' in key:
#         print(item)
#     # print('\n')



# warda code

warda = pandas.read_csv('SKU + EAN UPDATE - 07.12.2022 - filled - v3.xlsx - Bestellliste.csv')

for item in warda.to_dict().items():
    print(item)

produktkategorie = []
for key, value in warda.to_dict()['Produktkategorie'].items():
    produktkategorie.append(value)
print(len(produktkategorie))
produktbezeichnung1 = []
for key, value in warda.to_dict()['Produktbezeichnung1'].items():
    produktbezeichnung1.append(value)
print(len(produktbezeichnung1))
produktbezeichnung2 = []
for key, value in warda.to_dict()['Produktbezeichnung2'].items():
    produktbezeichnung2.append(value)
print(len(produktbezeichnung2))
ean = []
for key, value in warda.to_dict()['EAN'].items():
    ean.append(value)
print(len(ean))
artikelnummer = []
for key, value in warda.to_dict()['Artikelnummer'].items():
    artikelnummer.append(value)
print(len(artikelnummer))
anzahl_pro_verp = []
for key, value in warda.to_dict()['Anzahl\npro Verp.'].items():
    anzahl_pro_verp.append(value)
print(len(anzahl_pro_verp))
umverpackung__ve = []
for key, value in warda.to_dict()['Umverpackung/ VE'].items():
    umverpackung__ve.append(value)
print(len(umverpackung__ve))
farbvarianten = []
for key, value in warda.to_dict()['Farbvarianten'].items():
    farbvarianten.append(value)
print(len(farbvarianten))
verpackung = []
for key, value in warda.to_dict()['Verpackung'].items():
    verpackung.append(value)
print(len(verpackung))
ve_je_karton = []
for key, value in warda.to_dict()['VE je Karton'].items():
    ve_je_karton.append(value)
print(len(ve_je_karton))
gewicht__karton_kg = []
for key, value in warda.to_dict()['Gewicht/ Karton/KG'].items():
    gewicht__karton_kg.append(value)
print(len(gewicht__karton_kg))
gesamt__gewicht_palette_kg = []
for key, value in warda.to_dict()['Gesamt/ Gewicht Palette/KG'].items():
    gesamt__gewicht_palette_kg.append(value)
print(len(gesamt__gewicht_palette_kg))
kartons_auf_palette = []
for key, value in warda.to_dict()['Kartons auf Palette\n'].items():
    kartons_auf_palette.append(value)
print(len(kartons_auf_palette))
title =[]
for key, value in warda.to_dict()['title'].items():
    title.append(value)
print(len(title))
type = []
for key, value in warda.to_dict()['type'].items():
    type.append(value)
print(len(type))
weight = []
for key, value in warda.to_dict()['weight'].items():
    weight.append(value)
print(len(weight))
options = []
for key, value in warda.to_dict()['options'].items():
    options.append(value)
print(len(options))
image = []
for key, value in warda.to_dict()['image'].items():
    image.append(value)
print(len(image))
url = []
for key, value in warda.to_dict()['url'].items():
    url.append(value)
print(len(url))
cat = []
for key, value in warda.to_dict()['cat'].items():
    cat.append(value)
print(len(cat))
product_id = []
for key, value in warda.to_dict()['product_id'].items():
    product_id.append(value)
print(len(product_id))
product_title = []
for key, value in warda.to_dict()['product_title'].items():
    product_title.append(value)
print(len(product_title))
variant_title = []
for key, value in warda.to_dict()['variant_title'].items():
    variant_title.append(value)
print(len(variant_title))
variant_id = []
for key, value in warda.to_dict()['variant_id'].items():
    variant_id.append(value)
print(len(variant_id))
variant_sku = []
for key, value in warda.to_dict()['variant_sku'].items():
    variant_sku.append(value)
print(len(variant_sku))
tags = []
for key, value in warda.to_dict()['tags'].items():
    tags.append(value)
print(len(tags))
available = []
for key, value in warda.to_dict()['available'].items():
    available.append(value)
print(len(available))
requires_shipping = []
for key, value in warda.to_dict()['requires_shipping'].items():
    requires_shipping.append(value)
print(len(requires_shipping))
taxable = []
for key, value in warda.to_dict()['taxable'].items():
    taxable.append(value)
print(len(taxable))
content = []
for key, value in warda.to_dict()['content'].items():
    content.append(value)
print(len(content))
description = []
for key, value in warda.to_dict()['description'].items():
    description.append(value)
print(len(description))
images = []
for key, value in warda.to_dict()['images'].items():
    images.append(value)

print(len(images))
    # print(key)
# print(produktkategorie)

final_warda = {}


for n in range(len(variant_sku)):
    if str(produktkategorie[n]) != 'nan' and str(artikelnummer[n]) != 'nan':
        produktkategorie_temp = produktkategorie[n]
    else:
        pass
    if str(produktbezeichnung1[n]) != 'nan' and str(artikelnummer[n]) != 'nan':
        produktbezeichnung_temp = produktbezeichnung1[n]
    else:
        pass
    final_warda[variant_sku[n]] = {"Produktkategorie": [produktkategorie_temp],
                                   "Produktbezeichnung1": [produktbezeichnung_temp],
        "Produktbezeichnung2": [produktbezeichnung2[n]],
        "EAN": [ean[n]],
        "Artikelnummer": [artikelnummer[n]],
        "Anzahl\npro Verp.": [anzahl_pro_verp[n]],
        "Umverpackung/ VE": [umverpackung__ve[n]],
        "Farbvarianten": [farbvarianten[n]],
        "Verpackung": [verpackung[n]],
        "VE je Karton": [ve_je_karton[n]],
        "Gewicht/ Karton/KG": [gewicht__karton_kg[n]],
        "Gesamt/ Gewicht Palette/KG": [gesamt__gewicht_palette_kg[n]],
        "Kartons auf Palette\n": [kartons_auf_palette[n]],
        "title": [title[n]],
        "type": [type[n]],
        "weight": [weight[n]],
        "options": [options[n]],
        "image": [image[n]],
        "url": [url[n]],
        "cat": [cat[n]],
        "product_id": [product_id[n]],
        "product_title": [product_title[n]],
        "variant_title": [variant_title[n]],
        "variant_id": [variant_id[n]],
        "variant_sku":[variant_sku[n]],
        "tags": [tags[n]],
        "available": [available[n]],
        "requires_shipping": [requires_shipping[n]],
        "taxable": [taxable[n]],
        "content": [content[n]],
        "description": [description[n]],
        "images": [images[n]],
    }

# images code

ds = pandas.read_csv('BioMondi.xlsx - Recovered_Sheet1.csv')
URLs= []
Category= []
Title= []
Price= []
Variants= []
Stock= []
Description= []
Thumbnail_src= []
Images_1= []
Images_2= []
Images_3= []
Images_4= []
Images_5= []
Images_6= []
Images_7= []
Images_8= []
Images_9= []
Images_10= []
#
# for item in ds.keys():
#     print(item)

for keys, val in ds["URLs"].items():
    URLs.append(val)

for keys, val in ds["Category"].items():
    Category.append(val)

for keys, val in ds["Title"].items():
    Title.append(val)

for keys, val in ds["Price"].items():
    Price.append(val)

for keys, val in ds["Variants"].items():
    Variants.append(val)

for keys, val in ds["Stock"].items():
    Stock.append(val)

for keys, val in ds["Description"].items():
    Description.append(val)

for keys, val in ds["Thumbnail-src"].items():
    Thumbnail_src.append(val)

for keys, val in ds["Images-1"].items():
    Images_1.append(val)

for keys, val in ds["Images-2"].items():
    Images_2.append(val)

for keys, val in ds["Images-3"].items():
    Images_3.append(val)

for keys, val in ds["Images-4"].items():
    Images_4.append(val)

for keys, val in ds["Images-5"].items():
    Images_5.append(val)

for keys, val in ds["Images-6"].items():
    Images_6.append(val)

for keys, val in ds["Images-7"].items():
    Images_7.append(val)

for keys, val in ds["Images-8"].items():
    Images_8.append(val)

for keys, val in ds["Images-9"].items():
    Images_9.append(val)

for keys, val in ds["Images-10"].items():
    Images_10.append(val)

final_images = {}
for n in range(len(URLs)):
    if str(Thumbnail_src[n]) != 'nan':
        final_images[Thumbnail_src[n].split('v=')[-1]] = {
                'URLs': [URLs[n]],
        'Category': [Category[n]],
        'Title': [Title[n]],
        'Price': [Price[n]],
        'Variants': [Variants[n]],
        'Stock': [Stock[n]],
        'Description': [Description[n]],
        'Thumbnail - src': [Thumbnail_src[n]],
        'Images - 1': [Images_1[n]],
        'Images - 2': [Images_2[n]],
        'Images - 3': [Images_3[n]],
        'Images - 4': [Images_4[n]],
        'Images - 5': [Images_5[n]],
        'Images - 6': [Images_6[n]],
        'Images - 7': [Images_7[n]],
        'Images - 8': [Images_8[n]],
        'Images - 9': [Images_9[n]],
        'Images - 10': [Images_10[n]]
        }

    else:
        # print('empty')
        pass

for key, value in final_warda.items():
    for it, val in final_images.items():
        if str(it) in str(value):
            # temp_dict = {}
            for k, va in val.items():
                value[k] = va


for key, val in final_warda.items():
    if 'URLs' not in val:
        val['URLs']= [None]
        val['Category']= [None]
        val['Title']= [None]
        val['Price']= [None]
        val['Variants']= [None]
        val['Stock']= [None]
        val['Description']= [None]
        val['Thumbnail - src']= [None]
        val['Images - 1']= [None]
        val['Images - 2']= [None]
        val['Images - 3']= [None]
        val['Images - 4']= [None]
        val['Images - 5']= [None]
        val['Images - 6']= [None]
        val['Images - 7']= [None]
        val['Images - 8']= [None]
        val['Images - 9']= [None]
        val['Images - 10']= [None]
# for key, val in final_warda.items():
#     print(val)
#     break

final_file_ready_dataset = []
for key, value in final_b2bs.items():
    # both = False
    for it, val in final_warda.items():
        if str(key).split('-PAL')[0] in str(it):
            temp_dict = {}
            for k, va in val.items():
                if len(va) < value["Max len"]:
                    while len(va) < value["Max len"]:
                        va.append(None)
            for k, va in value.items():
                temp_dict[k] = va
            for k, va in val.items():
                temp_dict[k] = va
            final_file_ready_dataset.append(temp_dict)
# for item
last_dataset = {}
# print(final_file_ready_dataset[0])
for item, val in final_file_ready_dataset[0].items():
    last_dataset[str(item)] = []
for item in final_file_ready_dataset:

    for key, val in item.items():
        # print(key)
        try:
            last_dataset[key].extend(val)
        except:
        # print('max')
            pass
# for key, val in final_file_ready_dataset.items():
#     print(val)
#     break

# for item, va in last_dataset.items():
#     if item != 'Produktkategorie':
#         va.append(None)
#         va.append(None)
#     else:
#         break

# print(last_dataset)
last_dataset.pop('Max len')
# for item in final_file_ready_dataset:
for item, val in last_dataset.items():
    print(item, len(val))
df = pandas.DataFrame(last_dataset)
df.to_csv('fina.csv')




# fd = df.to_dict()
# print(df)

# with pandas.ExcelWriter('op.xlsx') as writer:
#     df.to_excel(writer, sheet_name='sheet1')
# # for value in b2b.to_dict()["SKU"]:
# #     print('
#     # break
# import time
# final_dict = {}
# wardas_data={}
# b2bs_data = {}
# items = {}
# pos = []
# for key,  column in b2b.to_dict()['Produktkategorie'].items():
#     pos.append(column)

#

# for item in result:
#     if len(item)
# print(result)

# for i in range(len(result)):
    # for item in result[i]
#
# sku = []
# for key,  column in b2b.to_dict()['Produktkategorie'].items():
#     sku.append(column)

# product_description = []
# for key,  column in b2b.to_dict()['Product Description'].items():
#     product_description.append(column)
#
# menge_unit_reference = []
# for key,  column in b2b.to_dict()['Produktbezeichnung'].items():
#     menge_unit_reference.append(column)


# produktvorteile = []
# for item, column in warda.to_dict()['Produktvorteile'].items():
#     produktvorteile.append(column)
# for item in sku:
# for item in range(len(sku))
#     nan = True
# result = []
# temp_list = []
# for i in produktvorteile:
#     if str(i) == 'nan':
#         # temp_list.append(i)
#         print(temp_list)
#         result.append(temp_list)
#         temp_list = []
#         # pass
#     else:
#         temp_list.append(i)
# result.append(temp_list)
# print(result)
# print(product_des)
# print(len(sku))
#Name	Published	Is featured?	Visibility in catalog	Short description	Description	Tax status	Tax class	In stock?	Stock	Regular price	Sale price	Categories	Tags	Shipping class	Images	Upsells	Cross-sells	Position	Tiered pricing type	Tiered pricing minimum product quantity	Fixed Tiered Prices	Percentage Tiered Prices	Supplier Id	Supplier Name	Supplier Slug	Supplier Description	Supplier Email	Supplier Account Number	Attribute 1 name	Attribute 1 value(s)	Attribute 1 visible	Attribute 1 global	Meta: min_quantity	Meta: max_quantity	Meta: rank_math_permalink	Meta: tabelle_zeile_1	Meta: _tabelle_zeile_1	Meta: tabelle_zeile_2	Meta: _tabelle_zeile_2	Meta: tabelle_zeile_3	Meta: _tabelle_zeile_3	Meta: tabelle_zeile_4	Meta: _tabelle_zeile_4	Meta: tabelle_zeile_5	Meta: _tabelle_zeile_5	Meta: tabelle_zeile_6	Meta: _tabelle_zeile_6	Meta: tabelle_zeile_7	Meta: _tabelle_zeile_7	Meta: tabelle_zeile_8	Meta: _tabelle_zeile_8	Meta: best_price	Meta: _best_price	Meta: best_price_comma	Meta: _best_price_comma	Meta: price_table_shortcode	Meta: _price_table_shortcode	Meta: minimum_allowed_quantity	Meta: group_of_quantity	Meta: allow_combination	Meta: minmax_do_not_count	Meta: minmax_cart_exclude	Meta: minmax_category_group_of_exclude	Meta: _is_ali_product	Meta: supplier	Meta: supplierid	Meta: _brands	Meta: _shipping_carrier	Meta: shipping_days_min	Meta: _shipping_days_min	Meta: shipping_days_max	Meta: _shipping_days_max	Meta: _vi_woo_product_variation_swatches_product_attribute	Meta: brands	Meta: shipping_carrier	Attribute 1 default	Attribute 2 name	Attribute 2 value(s)	Attribute 2 visible	Attribute 2 global	Attribute 2 default	Attribute 3 name	Attribute 3 value(s)	Attribute 3 visible	Attribute 3 global	Attribute 3 default	Attribute 4 name	Attribute 4 value(s)	Attribute 4 visible	Attribute 4 global	Meta: shipping_time	Meta: _shipping_time	Meta: custom_field_1_title	Meta: _custom_field_1_title	Meta: custom_field_1_desc	Meta: _custom_field_1_desc	Meta: custom_field_2_title	Meta: _custom_field_2_title	Meta: custom_field_2_desc	Meta: _custom_field_2_desc	Meta: custom_field_3_title	Meta: _custom_field_3_title	Meta: custom_field_3_desc	Meta: _custom_field_3_desc	Meta: custom_field_4_title	Meta: _custom_field_4_title	Meta: custom_field_4_desc	Meta: _custom_field_4_desc	Meta: custom_field_5_title	Meta: _custom_field_5_title	Meta: custom_field_5_desc	Meta: _custom_field_5_desc

