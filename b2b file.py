import pandas



b2b = pandas.read_csv('#B2B MASTER __ AUTO-CALCULATION - Biomondi.csv')


bb2 = str(pandas.read_csv('biomundi 2 b2b.csv').to_dict())
bbb3 = pandas.read_csv('biomundi 2 b2b.csv').to_dict()
#b2b code


bb3 = {}
b3_artical = []
price_per_pro_b3 = []
for key, item in bbb3["Artikelnummer"].items():
    if str(item).lower() != 'nan':
        b3_artical.append(str(int(item)))

for key, item in bbb3["Preis\n je Artikel (in EUR)"].items():
    if str(item).lower() != 'nan':
        price_per_pro_b3.append(item.replace(' €', ''))

for i in range(len(b3_artical)):
    try:
        bb3[b3_artical[i]] = price_per_pro_b3[i]
    except:
        print('already there')

print(bb3)
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
import time
item_len_num = []
for te in pos_numbers:
    item_len_num.append(len(te))
    # print(last_item)
# print(len(item_len_num))

final_b2bs = {}
start_num = 0

for item in range(len(item_len_num)):
    # print(sku[start_num])
    #
    # final_pro_quant
    # for
    # final_total_selling_check = total_selling_price[start_num: start_num + item_len_num[item]]
    if str(sku[start_num]).lower().replace('-pal', '') in bb2:
        finalpos = pos[start_num: start_num+item_len_num[item]]
        final_skus = sku[start_num: start_num+item_len_num[item]]
        final_pro_des = product_description[start_num: start_num + item_len_num[item]]
        final_menge = menge_unit_ref[start_num: start_num+item_len_num[item]]
        # print('flt', final_skus)
        l_purchase = purchase[start_num: start_num + item_len_num[item]][-1]
        purc_per_pc = bb3[final_skus[0].replace('-PAL', '')]
        final_purchase = [purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, purc_per_pc, l_purchase]
        # print('fly',final_purchase)
        final_shipping = shipping[start_num: start_num + item_len_num[item]]
        final_free_shipping = free_shipping[start_num: start_num + item_len_num[item]]
        final_purchase_incl_freight = purchace_incl_freight[start_num: start_num + item_len_num[item]]
        final_purchasing_total = purchasing_total[start_num: start_num + item_len_num[item]]
        final_margin_per = margin_per[start_num: start_num + item_len_num[item]]
        final_yield = yield_[start_num: start_num + item_len_num[item]]
        final_pro_quant = product_quant[start_num: start_num + item_len_num[item]]
        final_unique_selling = unique_selling_price[start_num: start_num + item_len_num[item]]
        final_total_selling = total_selling_price[start_num: start_num + item_len_num[item]]
        end_non_pal_tier = 0
        print(final_skus)
        print('pan')
    # break
        print(final_purchase)
        for en in range(len(final_total_selling)):
            if 'nan' not in str(final_total_selling[en]):
                purchasin_total = float(final_pro_quant[en]) * float(str(str(final_purchase[en]).replace(',', '.')))
                if purchasin_total < int(final_free_shipping[en]):
                    purchasin_total = purchasin_total + float(str(final_shipping[en]).replace(',', '.'))
                try:
                    final_purchasing_total[
                        en] = f"{str(float(purchasin_total)).replace('.', ',').split(',')[0]},{str(float(purchasin_total)).replace('.', ',').split(',')[1][:2]}"
                except:
                    final_purchasing_total[en] = str(float(purchasin_total)).replace('.', ',')
                # print('pal', final_purchasing_total[em])

                try:
                    final_purchase_incl_freight[
                        en] = f"{str(float(purchasin_total / int(final_pro_quant[en]))).replace('.', ',').split(',')[0]},{str(float(purchasin_total / int(final_pro_quant[en]))).replace('.', ',').split(',')[1][:2]}"
                except:
                    final_purchase_incl_freight[en] = str(float(purchasin_total / int(final_pro_quant[en]))).replace(
                        '.', ',')

                try:
                    final_yield[
                        en] = f"{str(float(purchasin_total * float(final_margin_per[en].replace(',', '.')))).replace('.', ',').split(',')[0]},{str(float(purchasin_total * float(final_margin_per[en].replace(',', '.')))).replace('.', ',').split(',')[1][:2]}"
                except:
                    final_yield[en] = str(
                        float(purchasin_total * float(final_margin_per[en].replace(',', '.')))).replace('.', ',')

                try:
                    final_unique_selling[
                        en] = f"{str(float(purchasin_total + float(final_yield[en].replace(',', '.'))) / int(final_pro_quant[en])).replace('.', ',').split(',')[0]},{str(float(purchasin_total + float(final_yield[en].replace(',', '.'))) / int(final_pro_quant[en])).replace('.', ',').split(',')[1][:2]}€"
                except:
                    final_unique_selling[
                        en] = f"{str(float(purchasin_total + float(final_yield[en].replace(',', '.'))) / int(final_pro_quant[en])).replace('.', ',')}€"

                try:
                    final_total_selling[
                        en] = f"{str(purchasin_total + float(final_yield[en].replace(',', '.'))).replace('.', ',').split(',')[0]},{str(purchasin_total + float(final_yield[en].replace(',', '.'))).replace('.', ',').split(',')[1][:2]}"
                except:
                    final_total_selling[
                        en] = f"{str(purchasin_total + float(final_yield[en].replace(',', '.'))).replace('.', ',')}"

        try:
            # end_non_pal_tier = float(str(purchasing_total[(start_num-2)]).replace(',', '.')) + 400
            if len(list(final_b2bs)) > 1:
                end_non_pal_tier = float(final_b2bs[list(final_b2bs)[-1]]['Purchasing Total'][-2].replace(',','.'))+400
            else:
                end_non_pal_tier = 4000
                print('4000 me ho gya')
            print('finas', end_non_pal_tier, final_b2bs[list(final_b2bs)[-1]]['Purchasing Total'])
            # print('endi', end_non_pal_tier, purchasing_total[(start_num): (start_num) + item_len_num[item - 1]])
            # print(purchasing_total[start_num: start_num + item_len_num[item]])
            # print()
            print('endi',end_non_pal_tier)
        except Exception as ex:
            # print()
            print(ex,'4000 me do')
            # time.sleep(3)
            end_non_pal_tier = 4000

        while True:
            pal = False
            non_pal = False
            less_100 = False
            stop_not_more = False
            break_yes_loop = False
            first_pur = final_purchasing_total[0]
            print('fina p ', first_pur)

            for em in range(len(final_total_selling)):
                # if 'nan' not in str(final_total_selling[em]):
                    # print('fina p',str(final_purchasing_total[0]))
                # print(purchasing_total[(start_num): (start_num) + item_len_num[item+1]])

                if float(str(first_pur).replace(',', '.')) > end_non_pal_tier and 'pal' in str(final_skus).lower() and 'nan' not in str(final_total_selling[em]):
                    anzal = final_pro_des[0].split('Verp. = ')[1]
                    if 'Stück' in final_pro_des[0]:
                        stuck = anzal.split('Stück')[0].replace(' ', '')
                    else:
                        stuck = anzal.split('Rollen')[0].replace(' ', '')
                    # stuck = anzal.split('Stück')[0].replace(' ', '')
                    if int(int(final_pro_quant[0]) - int(stuck)) < int(stuck):
                        pal = False
                        stop_not_more = True

                    else:
                        # print('dong pal +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                        pal = True
                        anzal = final_pro_des[0].split('VE je Karton = ')[1]
                        # anzal = final_pro_des[0].split('Verp. = ')[1] r

                        stuck = int(anzal.split(' ,')[0].replace(' ', ''))
                        if int(int(final_pro_quant[0])-int(stuck)) < int(stuck):
                            pal = False
                            stop_not_more = True
                        else:
                            final_pro_quant[em] = int(int(final_pro_quant[em])-int(stuck))
                        purchasin_total = float(final_pro_quant[em]) * float(str(final_purchase[em].replace(',', '.')))
                        if purchasin_total < int(final_free_shipping[em]):
                            purchasin_total = purchasin_total + float(str(final_shipping[em]).replace(',', '.'))
                        try:
                            final_purchasing_total[em] = f"{str(float(purchasin_total)).replace('.', ',').split(',')[0]},{str(float(purchasin_total)).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_purchasing_total[em] = str(float(purchasin_total)).replace('.', ',')
                        # print('pal', final_purchasing_total[em])

                        try:
                            final_purchase_incl_freight[em] = f"{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[0]},{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_purchase_incl_freight[em] = str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',')

                        try:
                            final_yield[em] = f"{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[0]},{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_yield[em] = str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',')

                        try:
                            final_unique_selling[em] =f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.')))/int(final_pro_quant[em])).replace('.',  ',').split(',')[0]},{str(float(purchasin_total + float(final_yield[em].replace(',', '.')))/int(final_pro_quant[em])).replace('.',  ',').split(',')[1][:2]}€"
                        except:
                            final_unique_selling[em] = f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.'))) / int(final_pro_quant[em])).replace('.', ',')}€"

                        try:
                            final_total_selling[em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[0]},{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_total_selling[em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',')}"
                elif float(str(first_pur).replace(',', '.')) > 40 and 'pal' not in str(final_skus).lower() and 'nan' not in str(final_total_selling[em]):
                    anzal = final_pro_des[0].split('Verp. = ')[1]
                    if 'Stück' in final_pro_des[0]:
                        stuck = anzal.split('Stück')[0].replace(' ', '')
                    else:
                        stuck = anzal.split('Rollen')[0].replace(' ', '')
                    # stuck = anzal.split('Stück')[0].replace(' ', '')
                    if int(int(final_pro_quant[0]) - int(stuck)) < int(stuck):
                        non_pal = False
                        stop_not_more = True
                    else:
                        anzal = final_pro_des[0].split('VE je Karton = ')[1]
                        # anzal = final_pro_des[0].split('Verp. = ')[1] r

                        stuck = anzal.split(' ,')[0].replace(' ', '')
                        # print('doing non pal +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=')
                        non_pal = True
                        if int(int(final_pro_quant[0])-int(stuck)) < int(stuck):
                            non_pal = False
                            stop_not_more = True
                        else:
                            final_pro_quant[em] = int(int(final_pro_quant[em])-int(stuck))
                        purchasin_total = float(final_pro_quant[em]) * float(str(final_purchase[em].replace(',', '.')))

                        if purchasin_total < int(final_free_shipping[em]):
                            purchasin_total = purchasin_total + float(str(final_shipping[em]).replace(',', '.'))
                        try:
                            final_purchasing_total[em] = f"{str(float(purchasin_total)).replace('.', ',').split(',')[0]},{str(float(purchasin_total)).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_purchasing_total[em] = str(float(purchasin_total)).replace('.', ',')


                        try:
                            final_purchase_incl_freight[em] = f"{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[0]},{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_purchase_incl_freight[em] = str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',')

                        try:
                            final_yield[em] = f"{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[0]},{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_yield[em] = str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',')

                        try:
                            final_unique_selling[em] =f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.')))/int(final_pro_quant[em])).replace('.',  ',').split(',')[0]},{str(float(purchasin_total + float(final_yield[em].replace(',', '.')))/int(final_pro_quant[em])).replace('.',  ',').split(',')[1][:2]}€"
                        except:
                            final_unique_selling[em] = f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.'))) / int(final_pro_quant[em])).replace('.', ',')}€"

                        try:
                            final_total_selling[em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[0]},{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_total_selling[em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',')}"

                elif float(str(first_pur).replace(',', '.')) < 40 and 'pal' not in str(final_skus).lower() and 'nan' not in str(final_total_selling[em]):
                    less_100 = True
                    # print('doing less 100 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=')
                    anzal = final_pro_des[0].split('VE je Karton = ')[1]
                    # anzal = final_pro_des[0].split('Verp. = ')[1] r

                    stuck = anzal.split(' ,')[0].replace(' ', '')
                    final_pro_quant[em] = int(int(final_pro_quant[em]) + int(stuck))
                    purchasin_total = float(final_pro_quant[em]) * float(str(final_purchase[em].replace(',', '.')))

                    if purchasin_total < int(final_free_shipping[em]):
                        purchasin_total = purchasin_total + float(str(final_shipping[em]).replace(',', '.'))
                    try:
                        final_purchasing_total[em] = f"{str(float(purchasin_total)).replace('.', ',').split(',')[0]},{str(float(purchasin_total)).replace('.', ',').split(',')[1][:2]}"
                    except:
                        final_purchasing_total[em] = str(float(purchasin_total)).replace('.', ',')
                    try:
                        final_purchase_incl_freight[em] = f"{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[0]},{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[1][:2]}"
                    except:
                        final_purchase_incl_freight[em] = str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',')

                    try:
                        final_yield[em] = f"{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[0]},{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[1][:2]}"
                    except:
                        final_yield[em] = str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',')

                    try:
                        final_unique_selling[em] =f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.')))/int(final_pro_quant[em])).replace('.',  ',').split(',')[0]},{str(float(purchasin_total + float(final_yield[em].replace(',', '.')))/int(final_pro_quant[em])).replace('.',  ',').split(',')[1][:2]}€"
                    except:
                        final_unique_selling[em] = f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.'))) / int(final_pro_quant[em])).replace('.', ',')}€"

                    try:
                        final_total_selling[em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[0]},{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[1][:2]}"
                    except:
                        final_total_selling[em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',')}"

                else:
                    if 'nan' not in str(final_total_selling[em]):
                        purchasin_total = float(final_pro_quant[em]) * float(str(str(final_purchase[em]).replace(',', '.')))

                        if purchasin_total < int(final_free_shipping[em]):
                            purchasin_total = purchasin_total + float(str(final_shipping[em]).replace(',', '.'))
                        try:
                            final_purchasing_total[
                                em] = f"{str(float(purchasin_total)).replace('.', ',').split(',')[0]},{str(float(purchasin_total)).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_purchasing_total[em] = str(float(purchasin_total)).replace('.', ',')
                        try:
                            final_purchase_incl_freight[
                                em] = f"{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[0]},{str(float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_purchase_incl_freight[em] = str(
                                float(purchasin_total / int(final_pro_quant[em]))).replace('.', ',')

                        try:
                            final_yield[
                                em] = f"{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[0]},{str(float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_yield[em] = str(
                                float(purchasin_total * float(final_margin_per[em].replace(',', '.')))).replace('.', ',')

                        try:
                            final_unique_selling[
                                em] = f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.'))) / int(final_pro_quant[em])).replace('.', ',').split(',')[0]},{str(float(purchasin_total + float(final_yield[em].replace(',', '.'))) / int(final_pro_quant[em])).replace('.', ',').split(',')[1][:2]}€"
                        except:
                            final_unique_selling[
                                em] = f"{str(float(purchasin_total + float(final_yield[em].replace(',', '.'))) / int(final_pro_quant[em])).replace('.', ',')}€"

                        try:
                            final_total_selling[
                                em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[0]},{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',').split(',')[1][:2]}"
                        except:
                            final_total_selling[
                                em] = f"{str(purchasin_total + float(final_yield[em].replace(',', '.'))).replace('.', ',')}"
                # print(final_pro_quant[em])
                # print(final_pro_des[0])
                if not pal and not non_pal and not less_100 and 'nan' not in str(final_total_selling[em]):
                    break_yes_loop = True
                    # print(final_skus)
                    break
            if stop_not_more:
                # print('stop notmore')
                break
            if break_yes_loop:
                # print('correct')
                # print(final_total_selling[0])
                break
            if pal and int(float(str(final_purchasing_total[0]).replace(',', '.'))) <= end_non_pal_tier:
                # print('com pal')
                # print('fi b2', float(str(final_purchasing_total[0]).replace(',', '.')))
                break
            elif non_pal and float(str(final_purchasing_total[0]).replace(',', '.')) <= 100:
                # print('comnon pal')
                # print('fi b2', float(str(final_purchasing_total[0]).replace(',', '.')))
                break
            elif less_100 and float(str(final_purchasing_total[0]).replace(',', '.')) >= 40:
                # print('com les 100')
                # print('fi b2', float(str(final_purchasing_total[0]).replace(',', '.')))
                break
            else:
                # print('fi b2', float(str(final_purchasing_total[0]).replace(',', '.')))
                print('not done')
            # break
            # pass
            # pass

        # time.sleep(3)

        final_b2bs[sku[start_num]] = {'SKU': final_skus,
                                 'Product Description': final_pro_des,
                                 'Menge / Unit (Reference)': final_menge,
                                 'Product Qty': final_pro_quant,
                                 'Purchase': final_purchase,
                                 'Shipping': final_shipping,
                                  'Free Shipping': final_free_shipping,
                                  'Purchace incl. Freight': final_purchase_incl_freight,
                                  'Purchasing Total': final_purchasing_total,
                                  'Margin %': final_margin_per,
                                  'Yield': final_yield,
                                  'Unique Selling Price': final_unique_selling,
                                  'Total Selling Price': final_total_selling
                                  }
    else:
        print('not added')
    start_num += item_len_num[item]

fina_b2b = {}
for key, val in final_b2bs.items():
    for i, k in val.items():
        fina_b2b[i] = []

for key, val in final_b2bs.items():
    for i, k in val.items():
        for values in k:
            fina_b2b[i].append(values)

#
ds = pandas.DataFrame(fina_b2b)
ds.to_csv('b235.csv')
#
#
# import time
#
# time.sleep(5)
# b2 = pandas.read_csv('b235.csv')
#
#
# sku = []
# for key,  column in b2.to_dict()['SKU'].items():
#     sku.append(column)
#
# product_description = []
# for key,  column in b2.to_dict()['Product Description'].items():
#     product_description.append(column)
#
# menge_unit_ref = []
# for key,  column in b2.to_dict()['Menge / Unit (Reference)'].items():
#     menge_unit_ref.append(column)
#
# product_quant = []
# for key,  column in b2.to_dict()['Product Qty'].items():
#     product_quant.append(column)
#
# purchase = []
# for key,  column in b2.to_dict()['Purchase'].items():
#     purchase.append(column)
#
# shipping = []
# for key,  column in b2.to_dict()['Shipping'].items():
#     shipping.append(column)
#
# free_shipping = []
# for key,  column in b2.to_dict()['Free Shipping'].items():
#     free_shipping.append(column)
#
# purchace_incl_freight = []
# for key,  column in b2.to_dict()['Purchace incl. Freight'].items():
#     purchace_incl_freight.append(column)
#
# purchasing_total = []
# for key,  column in b2.to_dict()['Purchasing Total'].items():
#     purchasing_total.append(column)
#
# margin_per = []
# for key,  column in b2.to_dict()['Margin %'].items():
#     margin_per.append(column)
#
# yield_ = []
# for key,  column in b2.to_dict()['Yield'].items():
#     yield_.append(column)
#
# unique_selling_price = []
# for key,  column in b2.to_dict()['Unique Selling Price'].items():
#     unique_selling_price.append(column)
#
# total_selling_price = []
# for key,  column in b2.to_dict()['Total Selling Price'].items():
#     total_selling_price.append(column)
#
#
#
# f3 = {}
#
# f3['SKU'] = []
# f3['Product Description'] = []
# f3['Menge / Unit (Reference)'] = []
# f3['Product Qty'] = []
# f3['Purchase'] = []
# f3['Shipping'] = []
# f3['Free Shipping'] = []
# f3['Purchace incl. Freight'] = []
# f3['Purchasing Total'] = []
# f3['Margin %'] = []
# f3['Yield'] = []
# f3['Total Selling Price'] = []
# f3['Unique Selling Price'] = []
#
# for item in range(len(sku)):
#     if str(shipping[item]) != 'nan':
#         f3['SKU'].append(sku[item])
#         f3['Product Description'].append(product_description[item])
#         f3['Menge / Unit (Reference)'].append(menge_unit_ref[item])
#         # if float(total_selling_price[item].replace(',', '.')) > 300 and '-pal' not in sku[item]:
#         f3['Product Qty'].append(product_quant[item])
#         f3['Purchase'].append(purchase[item])
#         f3['Shipping'].append(shipping[item])
#         f3['Free Shipping'].append(free_shipping[item])
#         f3['Purchace incl. Freight'].append(purchace_incl_freight[item])
#         f3['Purchasing Total'].append(purchasing_total[item])
#         f3['Margin %'].append(margin_per[item])
#         f3['Yield'].append(yield_[item])
#         f3['Total Selling Price'].append(total_selling_price[item])
#         f3['Unique Selling Price'].append(unique_selling_price[item])
#     else:
#         pass
# import pandas



