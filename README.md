# -Fibonacci-sequence-gambling-stategy
斐波那契数列的公平概率gambling策略验证


各位好，今日闲来无事看到一个视频博主讲述斐波那契数列的Gambling 策略，于是乎写了一段代码来验证其说法。
斐波那契数列简介(引用Wikepedia)：
斐波那契数（意大利语：Successione di Fibonacci），又译为菲波拿契数、菲波那西数、斐氏数、黄金分割数。所形成的数列称为斐波那契数列（意大利语：Successione di Fibonacci），又译为菲波拿契数列、菲波那西数列、斐氏数列、黄金分割数列。

在数学上，斐波那契数是以递归的方法来定义：

{ F_{0}=0}F_{0}=0
{ F_{1}=1}F_{1}=1
{ F_{n}=F_{n-1}+F_{n-2}}F_{n}=F_{{n-1}}+F_{{n-2}}（n≧2）
用文字来说，就是斐波那契数列由0和1开始，之后的斐波那契数就是由之前的两数相加而得出。首几个斐波那契数是：

1、 1、 2、 3、 5、 8、 13、 21、 34、 55、 89、 144、 233、 377、 610、 987……

该博主说法为如果有10000本金，可以用如下策略：

分四次为一个小组下注，任意一次失败就回归到第一次重新开始下注：
1. 下注300
2. 下注800
3. 下注500
4. 下注1300

从此以往反复，据其所述，在本金到达5000时退出，上不封顶，他经常可以赢至70000 ~ 80000 本着科学的求证精神，写了一个简单的python验证，
为了模拟赌场真实情况，我将手数限制在300手，假设进入了100000次赌场（which is riduculus）粗略估计结果如下：

Expected ruturn value 一直在10000左右徘徊，大部分时候小于10000，赢至70000更是在我们100000次进入赌场后一次都没有达到，这还是在赔率公平的情况下，
而我们都知道其实赌场的所有和荷官对赌的游戏赌场都占有一定的赔率优势，即使是21点的千分之一优势，放大到100000次以后仍然是一个可观的数字，会令我们的expected return 下降至9700左右。
所以通过科学的验证方法告诉了我们不存在所谓的赌博技巧，请各位热爱生活，小赌怡情，大赌是在与数学和概率做博弈，而我们永远站在劣势的一方，谢谢！

Hello everyone, I saw a video blogger talking about the Gambling strategy of the Fibonacci sequence today, so I wrote a piece of code to verify his statement.
Breif intro to the Fibonacci sequence (quoted from Wikepedia):
Fibonacci number (Italian: Successione di Fibonacci), also translated as Fibonacci number,  golden section number. The formed sequence is called Fibonacci sequence (Italian: Successione di Fibonacci).

Mathematically, Fibonacci numbers are defined recursively:

{ F_{0}=0}F_{0}=0
{ F_{1}=1}F_{1}=1
{ F_{n}=F_{n-1}+F_{n-2}}F_{n}=F_{{n-1}}+F_{{n-2}}（n≧2）
In words, the Fibonacci sequence starts with 0 and 1, and the subsequent Fibonacci numbers are obtained by adding the previous two numbers. The first few Fibonacci numbers are:

1、 1、 2、 3、 5、 8、 13、 21、 34、 55、 89、 144、 233、 377、 610、 987……

The blogger said that if you have $10,000 , you can use the following strategy:

Bet four times as a row , and return to the first one to start betting again after any failure:
1. Bet $300
2. Bet $800
3. Bet $500
4. Bet $1300

And repeat this stategy. According to him, he quit when the principal reaches 5,000. There is no upper limit. He said he can win $70,000 ~ $80,000 a lot of times. In the spirit of scientific verification, I wrote a simple python code to verify.
In order to simulate the real situation of the casino, I limit the number of hands to 300, assuming that I have entered the casino 100,000 times (which is riduculus). The rough estimation results are as follows:

The expected return value has been hovering around 10,000, and most of the time it is less than 10,000. We have not reached 70,000 after we entered the casino for 100,000 times. This is still under the condition of fair odds.
And we all know that in fact, all casinos have a certain odds advantage. Even if it is a one-thousandth advantage of blackjack, it is still a considerable number after being enlarged to 100,000 times, which will make us The expected return dropped to around $9700.
Therefore, scientific verification methods tell us that there is no so-called gambling skills. Please love life and enjoy small bets. Big bets are a game with mathematics and probability, and we will always be on the disadvantaged side. Thank you!
