import math

import numpy as np
from Util.StringUtil import getRandomStr
import jieba
import torch
from torch import tensor


# print(torch.__version__)
# print(torch)
#
# a = torch.empty(5, 3)
# b = torch.rand(5, 3)
# c = torch.zeros(5, 3, dtype=torch.long)
# d = torch.ones(5, 3, dtype=torch.long)
# print(a), print(b), print(c), print(d)
# print(a.size()), print(b.size()), print(c.size()), print(d.size())
#
# tensor = torch.rand(3, 4)
# print(f"张量的形状：{tensor.shape}")
# print(f"张量的数据类型：{tensor.dtype}")
# print(f"张量的运算形式：{tensor.device}")
#
# a = torch.rand(5, 3)
# print(a)
# b = torch.ones(5, 3, dtype=torch.long)
# print(a + b), print(a - b), print(a * b), print(a / b)
# print(a.view(1, 15))
#
# data = [[1, 2], [3, 4]]
# n = np.array(data)
# t = torch.from_numpy(n)
# t1 = torch.tensor(n)
# n1 = t.numpy()
# print(n), print(t), print(t1), print(n1)
# print(type(n)), print(type(t)), print(type(t1)), print(type(n1))
#
# a = torch.ones(4, 4)
# print(torch.numel(a))  # 元素个数（大小）
# print(torch.eye(5))  # 对角线为1
# print(a.view(16))  # 同reshape
# b = torch.transpose(a, 0, 1)
# print(b)  # 维度交换
# a = torch.tensor(4)
# print(a.item())  # tensor维度为0时才有效
# print(a.int())  # 数据类型转换

# t1 = torch.arange(4).reshape(1, 4)
# t2 = torch.arange(9, 13).reshape(4, 1)
# print("*:", t1 * t2)
#
# t1 = torch.arange(4).reshape(1, 4)
# t2 = torch.arange(9, 10).reshape(1, 1)
# print("mul:", torch.mul(t1, t2))
# print("multiply:", torch.multiply(t1, t2))
#
# t1 = torch.arange(4).reshape(1, 4)
# t2 = torch.arange(9, 13).reshape(4, 1)
# print("mul:", torch.mul(t1, t2))
# print("multiply:", torch.multiply(t1, t2))
#
# t1 = torch.arange(8).reshape(2, 4)
# t2 = torch.arange(9, 11).reshape(2, 1)
# print("mul:", torch.mul(t1, t2))
# print("multiply:", torch.multiply(t1, t2))

# a = torch.arange(1, 7).reshape(2, 3)
# b = torch.arange(7, 13).reshape(3, 2)
# # a的行与b的列分别相乘
# print("mm:", torch.mm(a, b))

# t1 = torch.tensor([[1, 2, 3]])
# t2 = torch.tensor([[4, 5, 6]])
# print("dot:", torch.dot(t1, t2))


# t1 = torch.tensor([[1, 2, 3]])
# t2 = torch.tensor([[4, 5, 6]])
# print("inner:", torch.inner(t1, t2))
#
# t1 = torch.torch.arange(1, 5).reshape(2, 2)
# t2 = torch.torch.arange(5, 9).reshape(2, 2)
# print(t1, t2)
# # [[1*5+2*6,1*7+2*8],[3*5+4*6,3*7+4*8]]
# print("inner_D:", torch.inner(t1, t2))

# a = torch.arange(1, 28).reshape(3, 3, 3)
# print(a)
# # 2维以上x.T已过时，使用x.mT
# # print(a.T)
# print(a.mT)

# a = torch.tensor([[1], [2]])
# b = torch.tensor([[3], [4]])
# c = torch.cat([a, b], 0)
# d = torch.cat([a, b], 1)
# print(a), print(b)
# print(c), print(d)

# x = torch.zeros(2, 3, 2, 3, 2)
# x_1 = torch.zeros(2, 1, 2, 1, 2)
#
# x1 = torch.squeeze(x)
# x2 = torch.squeeze(x_1)
# print(x_1)
# print(x2)
# print(x.size(), "---->", x1.size())
# print(x_1.size(), "---->", x2.size())

# x = torch.arange(1, 10).reshape(3, 3)
# # print(x)
#
# a, b, c = x.split(1, 1)
# print(a)
# print(b)
# print(c)
# a, b = x.split(2, 1)
# print(a, b)

# print(np.log10(0.1))
# print(math.log(0.1))
# print(math.log10(0.1))
# print(math.log(0.1))
# print(torch.log10(tensor(0.1)).item())
# print(torch.log(tensor(0.1)).item())

# def get_ent(x):
#     ent = 0.0
#     for i in x:
#         ent -= i * np.log(i)
#     return ent
#
#
# x = np.array([1])
# x2 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# print(get_ent(x))
# print(get_ent(x2))


# def get_words_ent(word_arr):
#     length = len(word_arr)
#     dataDict = {}
#     for i in word_arr:
#         if dataDict.get(1) is None:
#             dataDict[i] = 1
#         else:
#             dataDict[i] += 1
#     return sum([-d / length * np.log(d / length) for d in list(dataDict.values())])
#
#
# en = jieba.lcut(r"""I am happy to join with you today in what will go down in history as the greatest demonstration
# for freedom in the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand
# today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions
# of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the
# long night of bad captivity.
#
# But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still
# sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later,
# the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years
# later, the Negro is still languished in the corners of American society and finds himself an exile in his own land.
# And so we've come here today to dramatize a shameful condition. In a sense we've come to our nation's capital to cash
# a check. When the architects of our republic wrote the magnificent words of the Constitution and the Declaration of
# Independence, they were signing a promissory note to which every American was to fall heir. This note was a promise
# that all men, yes, black men as well as white men, would be guaranteed the "unalienable Rights" of "Life, Liberty and
# the pursuit of Happiness." It is obvious today that America has defaulted on this promissory note, insofar as her
# citizens of color are concerned. Instead of honoring this sacred obligation, America has given the Negro people a bad
# check, a check which has come back marked "insufficient funds." But we refuse to believe that the bank of justice is
# bankrupt. We refuse to believe that there are insufficient funds in the great vaults of opportunity of this nation.
# And so, we've come to cash this check, a check that will give us upon demand the riches of freedom and the security
# of justice. We have also come to this hallowed spot to remind America of the fierce urgency of Now. This is no time
# to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real
# the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit
# path of racial justice. Now is the time to lift our nation from the quicksands of racial injustice to the solid rock
# of brotherhood. Now is the time to make justice a reality for all of God's children. It would be fatal for the nation
# to overlook the urgency of the moment. This sweltering summer of the Negro's legitimate discontent will not pass
# until there is an invigorating autumn of freedom and equality. Nineteen sixty-three is not an end, but a beginning.
# And those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the
# nation returns to business as usual. And there will be neither rest nor tranquility in America until the Negro is
# granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until
# the bright day of justice emerges. But there is something that I must say to my people, who stand on the warm
# threshold which leads into the palace of justice: In the process of gaining our rightful place, we must not be guilty
# of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and
# hatred. We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our
# creative protest to degenerate into physical violence. Again and again, we must rise to the majestic heights of
# meeting physical force with soul force. The marvelous new militancy which has engulfed the Negro community must not
# lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today,
# have come to realize that their destiny is tied up with our destiny. And they have come to realize that their freedom
# is inextricably bound to our freedom. We cannot walk alone. And as we walk, we must make the pledge that we shall
# always march ahead. We cannot turn back. There are those who are asking the devotees of civil rights, "When will you
# be satisfied?" We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police
# brutality. We can never be satisfied as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in
# the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negro's basic mobility
# is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their
# selfhood and robbed of their dignity by signs stating "for whites only." We cannot be satisfied as long as a Negro in
# Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote. No, no, we are not
# satisfied, and we will not be satisfied until "justice rolls down like waters, and righteousness like a mighty
# stream." I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have
# come fresh from narrow jail cells. And some of you have come from areas where your quest -- quest for freedom left
# you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans
# of creative suffering. Continue to work with the faith that unearned suffering is redemptive. Go back to Mississippi,
# go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and
# ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the
# valley of despair, I say to you today, my friends. And so even though we face the difficulties of today and tomorrow,
# I still have a dream. It is a dream deeply rooted in the American dream. I have a dream that one day this nation will
# rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are
# created equal." I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of
# former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day even
# the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression,
# will be transformed into an oasis of freedom and justice. I have a dream that my four little children will one day
# live in a nation where they will not be judged by the color of their skin but by the content of their character. I
# have a dream today! I have a dream that one day, down in Alabama, with its vicious racists, with its governor having
# his lips dripping with the words of "interposition" and "nullification" -- one day right there in Alabama little
# black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.
# I have a dream today! I have a dream that one day every valley shall be exalted, and every hill and mountain shall be
# made low, the rough places will be made plain, and the crooked places will be made straight; "and the glory of the
# Lord shall be revealed and all flesh shall see it together." This is our hope, and this is the faith that I go back
# to the South with. With this faith, we will be able to hew out of the mountain of despair a stone of hope. With this
# faith, we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood.
# With this faith, we will be able to work together, to pray together, to struggle together, to go to jail together,
# to stand up for freedom together, knowing that we will be free one day. And this will be the day -- this will be the
# day when all of God's children will be able to sing with new meaning: My country 'tis of thee, sweet land of liberty,
# of thee I sing. Land where my fathers died, land of the Pilgrim's pride, From every mountainside, let freedom ring!
# And if America is to be a great nation, this must become true. And so let freedom ring from the prodigious hilltops
# of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening
# Alleghenies of Pennsylvania. Let freedom ring from the snow-capped Rockies of Colorado. Let freedom ring from the
# curvaceous slopes of California. But not only that: Let freedom ring from Stone Mountain of Georgia. Let freedom ring
# from Lookout Mountain of Tennessee. Let freedom ring from every hill and molehill of Mississippi. From every
# mountainside, let freedom ring. And when this happens, when we allow freedom ring, when we let it ring from every
# village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's
# children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing
# in the words of the old Negro spiritual: Free at last! Free at last! Thank God Almighty, we are free at last!""")
# zh = jieba.lcut(r"""一百年前，一位伟大的美国人签署了《解放黑奴宣言》，今天我们就是在他的雕像前集会。这一庄严宣言犹如灯塔的光芒，给千百万在那
# 摧残生命的不义之火中受煎熬的黑奴带来了希望。它之到来犹如欢乐的黎明，结束了束缚黑人的漫长之夜。然而一百年后的今天，我们必须正视黑人还没有得到自由
# 这一悲惨的事实。一百年后的今天，在种族隔离的镣铐和种族歧视的枷锁下，黑人的生活备受压榨；一百年后的今天，黑人仍生活在物质充裕的海洋中一个穷困的孤
# 岛上；一百年后的今天，黑人仍然萎缩在美国社会的角落里，并且，意识到自己是故土家园中的流亡者。今天我们在这里集会，就是要把这种骇人听闻的情况公之于
# 众。就某种意义而言，今天我们是为了要求兑现诺言而汇集到我们国家的首都来的。我们共和国的缔造者草拟宪法和独立宣言时，曾以气壮山河的词句向每一个美国
# 人许下了诺言，他们承诺给予所有的人以不可剥夺的生存、自由和追求幸福的权利。就有色公民而论，美国显然没有实践她的诺言。美国没有履行这项神圣的义务，
# 只是给黑人开了一张空头支票，支票上盖上“资金不足”的戳子后便退了回来。但是我们不相信正义的银行已经破产，我们不相信，在这个国家巨大的机会之库里已没
# 有足够的储备。因此今天我们要求将支票兑现，这张支票——将给予我们宝贵的自由和正义的保障。我们来到这个圣地也是为了提醒美国，现在是非常急迫的时刻。现
# 在决非侈谈冷静下来或服用渐进主义的镇静剂的时候。现在是实现民主的诺言的时候。现在是从种族隔离的荒凉阴暗的深谷攀登种族平等的光明大道的时候，现在是
# 向上帝所有的儿女开放机会之门的时候。如果美国忽视时间的迫切性和低估黑人的决心，那么，这对美国来说，将是致命伤。自由和平等的爽朗秋天如不到来，黑人
# 义愤填膺的酷暑就不会过去。1963年并不意味着斗争的结束，而是开始。有人希望，黑人只要撒撒气就会满足；如果国家安之若素，毫无反应，这些人必会大失所望
# 的。黑人得不到公民的权利，美国就不可能有安宁或平静；正义的光明的一天不到来，叛乱的旋风就将继续动摇这个国家的基础。但是对于等候在正义之宫门口的心
# 急如焚的人们，有些话我是必须说的。在争取合法地位的过程中，我们不要采取错误的做法。我们不要为了满足对自由的渴望而抱着敌对和仇恨之杯痛饮。我们斗争
# 时必须永远举止得体，纪律严明。我们不能容许我们的具有崭新内容的抗议蜕变为暴力行动。我们要不断地升华到以精神力量对付物质力量的崇高境界中去。现在黑
# 人社会充满着了不起的新的战斗精神，但是我们却不能因此而不信任所有的白人。因为我们的许多白人兄弟已经认识到，他们的命运与我们的命运是紧密相连的，他
# 们今天参加游行集会就是明证；他们的自由与我们的自由是息息相关的。我们不能单独行动。当我们行动时，我们必须保证向前进。我们不能倒退。现在有人问热心
# 民权运动的人，“你们什么时候才能满足？”只要黑人仍然遭受警察难以形容的野蛮迫害，我们就绝不会满足。只要我们在外奔波而疲乏的身躯不能在公路旁的汽车旅
# 馆和城里的旅馆找到住宿之所，我们就绝不会满足。只要黑人的基本活动范围只是从少数民族聚居的小贫民区转移到大贫民区，我们就绝不会满足。只要密西西比仍
# 然有一个黑人不能参加选举，只要纽约有一个黑人认为他投票无济于事，我们就绝不会满足。不！我们现在并不满足，我们将来也不满足，除非正义和公正犹如江海
# 之波涛，汹涌澎湃，滚滚而来。我并非没有注意到，参加今天集会的人中，有些受尽苦难和折磨；有些刚刚走出窄小的牢房，有些由于寻求自由，曾在居住地惨遭疯
# 狂迫害的打击，并在警察暴行的旋风中摇摇欲坠。你们是人为痛苦的长期受难者。坚持下去吧，要坚决相信，忍受不应得的痛苦是一种赎罪。让我们回到密西西比去
# ，回到阿拉巴马去，回到南卡罗来纳去，回到佐治亚去，回到路易斯安那去，回到我们北方城市中的贫民区和少数民族居住区去，要心中有数，这种状况是能够也必
# 将改变的。我们不要陷入绝望而不可自拔。朋友们，今天我对你们说，在现在和未来，我们虽然遭受种种困难和挫折，我仍然有一个梦想。这个梦想是深深扎根于美
# 国的梦想中的。我梦想有一天，这个国家会站立起来，真正实现其信条的真谛：“我们认为这些真理是不言而喻的——人人生而平等。”我梦想有一天，在佐治亚州的红
# 色山岗上，昔日奴隶的儿子将能够和昔日奴隶主的儿子同席而坐，共叙手足情谊。我梦想有一天，甚至连密西西比州这个正义匿迹，压迫成风的地方，也将变成自由
# 和正义的绿洲。我梦想有一天，我的四个孩子将在一个不是以他们的肤色，而是以他们的品格优劣来评价他们的国度里生活。我今天有一个梦想。我梦想有一天，亚
# 拉巴马州能够有所转变，尽管该州州长现在仍然满口异议，反对联邦法令，但有朝一日，那里的黑人男孩和女孩将能与白人男孩和女孩情同骨肉，携手并进。我今天
# 有一个梦想。我梦想有一天，幽谷上升，高山下降，坎坷曲折之路成坦途，圣光披露，满照人间。这就是我们的希望。我怀着这种信念回到南方。有了这个信念，我
# 们将能从绝望之嶙劈出一块希望之石。有了这个信念，我们将能把这个国家刺耳争吵的声，改变成为一支洋溢手足之情的优美交响曲。有了这个信念，我们将能一起
# 工作，一起祈祷，一起斗争，一起坐牢，一起维护自由；因为我们知道，终有一天，我们是会自由的。在自由到来的那一天，上帝的所有儿女们将以新的含义高唱这
# 支歌：“我的祖国，美丽的自由之乡，我为您歌唱。您是父辈逝去的地方，您是最初移民的骄傲，让自由之声响彻每个山冈。”如果美国要成为一个伟大的国家，这
# 个梦想必须实现。让自由之声从新罕布什尔州的巍峨峰巅响起来！让自由之声从纽约州的崇山峻岭响起来！让自由之声从宾夕法尼亚州阿勒格尼山的顶峰响起来！""")
# wo = list(getRandomStr(10, digits=False))
# wo2 = list(getRandomStr(15, digits=False))
# # print(wo)
# # print(wo2)
# print(get_words_ent(en))
# print(get_words_ent(zh))


def cross_entropy(x, y):
    x = np.float_(x)
    y = np.float_(y)
    print(x)
    print(y)
    xo = x * np.log(y)
    yo = (1 - x) * np.log(1 - y)
    print(xo)
    print(yo)
    return -np.sum(xo + yo)


x1 = [(1, 1, 0), (0.5, 0.6, 0.7)]
x2 = [(0, 1, 1), (0.9, 0.4, 0.2)]
print(cross_entropy(x1[0], x1[1]))
print(cross_entropy(x2[0], x2[1]))
