#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import chardet
import jieba

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dight2hanzi = {'0':'零', '1': '一', '2':'二', '3':'三', '4':'四', '5':'五', '6':'六', '7':'七', '8':'八', '9': '九'}

reload(sys)
sys.setdefaultencoding("utf-8")


def chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


def srttime(time):
    t = time.strip()
    ts = t.split(',')
    r = 0
    r = r + int(ts[1])
    ts = ts[0].split(':')
    r = r + 1000 * (int(ts[0]) * 3600 + int(ts[1]) * 60 + int(ts[2]))
    return r


def cvgen(fn, fno):
    print(fn, fno)
    with open(fn, 'r') as fp:
        all = fp.read()
        dec = chardet.detect(all)['encoding']
        print(dec)

        cc = []
        with open(fn, 'r') as fp2:
            cc = fp2.readlines()

        cc = [c.decode(dec) for c in cc]

        print('lines', len(cc))

        # unicode begin
        tmp = []
        items = []
        for l in cc:
            if len(l) <= 2:
                if len(tmp) >= 3:
                    items.append(tmp)
                tmp = []

            else:
                tmp.append(l)

        print('cps', len(items))
        cps = []
        for item in items:
            cp = {}
            cp['t'] = item[1]
            cp['c'] = item[2]
            cps.append(cp)

        for cp in cps:
            pass
            #print cp['t']


        #去掉带有这些关键字的条目
        dirty_keys = [u'字幕', u'时间轴', u'压缩', u'翻译', u'后期', u'监制', u'上集', u'<', u'>', u'=', u'【', u'[', u'*', u'■', u'校对', '{']

        ncps = []
        for cp in cps:
            good = True
            for k in dirty_keys:
                if k in cp['c']:
                    good = False
                    break
            if good:
                ncps.append(cp)

        print("ncps", len(ncps))


        currt = -1000000


        ret = []
        cnt = 0

        for cp in ncps:
            ts = cp['t'].split(u'-->')
            startt = srttime(ts[0])
            endt = srttime(ts[1])


            SPLIT_INTERVAL = 1000
            if cnt < 2:
                SPLIT_INTERVAL = 5000
            elif cnt < 3:
                SPLIT_INTERVAL = 2000

            if startt - currt > SPLIT_INTERVAL:
                #new conv
                #ret.append(u'E\n')
                cnt = 0

            ret.append(u'M ' + cp['c'])
            cnt = cnt + 1
            currt = endt

        #拆分 --aaaaaaaa  --bbbbbb 这种同行但是多句的
        nret = []
        for r in ret:
            if u'-' in r:
                cs = (r[1:-1]).split(u'-')
                for c in cs:
                    a = c.strip()
                    if len(a) >= 2:
                        nret.append(a+"\n")

            else:
                nret.append(r)


        #分词
        nnret = []
        
        for r in nret:
            if len(r) >= 3:
                d = r[2:-2]

                #print(d)

                #ww = jieba.cut(d, cut_all=False)
                ww = []
                for w in d:
                    #print(w)
                    if w in digits:
                        ww.append(dight2hanzi[w])
                    else:
                        if chinese(w):
                            ww.append(w)
                if len(ww) < 5:
                    continue
                #ww = [w.strip() for w in ww]

                #print(ww)
                nl = "".join(ww[:])
                nnret.append(nl+"\n")
            else:
                nnret.append(r)

        with open(fno, 'w') as fpo:
            for r in nnret:
                fpo.write(r.encode('utf-8'))



if __name__ == "__main__":

    usage = 'USAGE  ./cvgen.py target.srt output.conv'
    if len(sys.argv) != 3:
        print(usage)
        exit()


    cvgen(sys.argv[1], sys.argv[2])
