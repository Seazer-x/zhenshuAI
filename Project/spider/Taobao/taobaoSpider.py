import requests


def getPage(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'cna=oZx8G8SkNzwCAbffkFgXxn8P; _samesite_flag_=true; cookie2=1759a0f13ec171059670404fb1947ef8; t=d31570ba21bb030643cce95d18f0eb4e; _tb_token_=e9f31894ebebb; xlly_s=1; sgcookie=E100zmxnjPbH7KFS6p6VNyXrnbji6b8mbUKfqJEni+QfwmEFvF7IvaEnI3iEEIdsMrEPSs7UOg8HzdfBdEvEOzyDeK8MN59wd/YB7Vewnq/P24o=; unb=3089806710; uc1=pas=0&cookie15=VT5L2FSpMGV7TQ==&existShop=false&cookie14=UoeyCUDDp7SnSg==&cookie16=VFC/uZ9az08KUQ56dCrZDlbNdA==&cookie21=UIHiLt3xThH8t7YQoFNq; uc3=lg2=VFC/uZ9ayeYq2g==&nk2=F6k3HMo9stdBPNZskZrjbj9fSkM=&vt3=F8dCv4oaxbxff4uMVp0=&id2=UNDcQ8Qhj9GGog==; csg=0a4461d6; lgc=t_1487572951471_0249; cancelledSubSites=empty; cookie17=UNDcQ8Qhj9GGog==; dnk=t_1487572951471_0249; skt=5fca39bd7ea26d34; existShop=MTY2NzEzODExOQ==; uc4=nk4=0@FbMocpyN+qTRCXjqGWbLRJCldUdcC4xeke5a56T0Jw==&id4=0@UgcsqYO7EUZxIPxalYcRivFePprR; tracknick=t_1487572951471_0249; _cc_=URm48syIZQ==; _l_g_=Ug==; sg=90f; _nk_=t_1487572951471_0249; cookie1=BxMCxFJHtrfH3ZERue91CB9DO+RT+ISR/KqaJ144kfA=; enc=moPa5GbS9CppRjg0JC+y3ECSr6n16BwHv3i1qxAksHUmewW73VEdur6qGLvnC+cxk3qlGItj8TX01cT2OC2Yng==; JSESSIONID=B98F9DCCB5685C5F83641398EB220284; isg=BKys-66I4yGAsvcdNPfZ79D6fYzeZVAP6md3RQbtuNf6EUwbLnUgn6KhNdmpgohn; l=eBaeydeVTzBfSpFEBOfanurza77OSIRYYuPzaNbMiOCPOs1B5nROW6yepQ86C3GVh6nHR3R5j0Q6BeYBcQOSnxv92j-la_kmn; tfstk=crP5BgZQtkF4PSCHZ0_VY8QfwQhdwsLsRTiuPgtW1NTEIc10kCo1xfeHvXuKl; _m_h5_tk=88850fd28df7ebfdfcdf8abe734f5196_1667147125145; _m_h5_tk_enc=aa361d106b21ca4e693e5292800d0dc9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52 '
    }
    session = requests.session()
    session.headers = header
    response = session.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response
    else:
        return "响应失败！"


if __name__ == '__main__':
    text = getPage("https://s.taobao.com/search?spm=a21bo.jianhua.201867-main.14.d1a111d91z52xn&q=%E6%95%B0%E7%A0%81")
    with open("taobao.txt", "w", encoding='utf-8') as f:
        f.write(text.text)
        f.close()
