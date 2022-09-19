from manim import *
from numpy import *


def set_colour(some_color):
    return some_color


class NewScene(Scene):
    def construct(self):
        
        a = Axes()
        graph = a.plot(lambda x: 2*x-3, color=BLUE)
        self.add(a, graph)
        
        # s = MathTex(r'S_{t.b}=S_{b.b}+2 S_{t}').scale(2).set_color(YELLOW)
        # stb = MathTex(r'S_{t.b}-\text{tolyq betinin audany}').scale(0.8).set_color(TEAL_E).move_to(DOWN+LEFT*3)
        # sbb = MathTex(r'S_{b.b}-\text{buiir betinin audany}').scale(0.8).set_color(TEAL_E).move_to(DOWN*2+LEFT*3)
        # st = MathTex(r'S_{t}-\text{taban audany}').scale(0.8).set_color(TEAL_E).move_to(DOWN*3+LEFT*3)
        # s1 = MathTex(r'S_{t.b}=', r'2\pi rh', r'+', r'2\pi r^2').scale(2).set_color(YELLOW)
        # b1 = Brace(s1[1], UP)
        # b1t = b1.get_text('buiir betinin audany')
        # b2 = Brace(s1[3], DOWN)
        # b2t = b2.get_text('taban audany')
        # g = VGroup(b1, b1t, b2, b2t)
        # self.wait()
        # self.play(Write(s), Write(stb), Write(sbb), Write(st))
        # self.wait(2)
        # self.play(ReplacementTransform(s, s1))
        # self.play(Create(g))
        # self.wait()
        # self.play(FadeOut(s1, shift=DOWN), FadeOut(g, shift=UP), FadeOut(stb, shift=LEFT), FadeOut(sbb, shift=LEFT), FadeOut(st, shift=LEFT))
        # self.wait()
        # v = MathTex(r'V=\pi r^2 h').scale(2).set_color(YELLOW)
        # self.play(FadeIn(v, shift=UP))
        # self.wait()

        # py = MathTex(r'a^2+b^2=c^2').scale(2).set_color(YELLOW)
        # a = MathTex(r'a=\sqrt{c^2-b^2}')
        # b = MathTex(r'b=\sqrt{c^2-a^2}')
        # c = MathTex(r'c=\sqrt{a^2+b^2}')
        # abc = VGroup(a, b, c).set_color(PURE_GREEN).arrange(1)
        
        # self.wait()
        # self.play(FadeIn(py, shift=UP))
        # self.wait(3)
        # self.play(FadeOut(py, shift=DOWN))
        # self.play(FadeIn(abc, shift=UP))
        # self.wait()


        # p1 = np.array([-1, 2, 0])
        # p2 = np.array([-1, -1, 0])
        # p3 = np.array([2, -1, 0])

        # l1 = Line(p1, p2)
        # l2 = Line(p2, p3)
        # l3 = Line(p3, p1)

        # p1d = Dot(p1).set_color(GREEN)
        # p2d = Dot(p2).set_color(GREEN)
        # p3d = Dot(p3).set_color(GREEN)

        # ra = RightAngle(l1, l2, quadrant=(-1, 1), length=0.4)

        # t = Text('Тік бұрышты үшбұрыш').scale(0.6)
        # k1 = Text('Катет').set_color(RED_E).move_to(LEFT*2)
        # k2 = Text('Катет').set_color(BLUE_E).move_to(DOWN*1.5)
        # k3 = Text('Гипотенуза').set_color(GREEN_E).move_to(RIGHT*2+UP)
        # a = Text('a').set_color(RED_E).move_to(LEFT*1.2+UP)
        # b = Text('b').set_color(BLUE_E).move_to(DOWN*1.5)
        # c = Text('c').set_color(GREEN_E).move_to(RIGHT*0.9+UP)

        # tr = Polygon(p1, p2, p3).set_color(TEAL_C)
        
        # p = MathTex(r'P=a+b+c').move_to(RIGHT*3+UP).set_color(GOLD_C)
        # S = MathTex(r'S=\frac{ab}{2}').move_to(RIGHT*3).set_color(BLUE_C)

        # self.play(Create(p1d),Create(p2d),Create(p3d))
        # self.play(Create(tr))
        # self.play(Create(ra))
        # self.wait()
        # self.play(Write(k1), Write(k2), Write(k3))
        # self.wait()
        # self.play(ReplacementTransform(k1, a), ReplacementTransform(k2, b), ReplacementTransform(k3, c))
        # self.wait(2)
        # self.play(Write(p))
        # self.wait()
        # self.play(Write(S))
        # self.wait()




        # l1 = Line(p1, np.array([0, -1, 0]), color=GREEN_E)
        # tc = Text('Биіктік с-ға түскеннен соң формулада с жазылады').scale(0.3).set_color(RED).move_to(DOWN*1.5+RIGHT*4)

        # a = Text('a').move_to(LEFT+UP)
        # b = Text('a').move_to(RIGHT+UP)
        # c = Text('c').move_to(DOWN*1.5)
        # h = Text('h').move_to(LEFT*0.5)
        # cm = Text('5').move_to(DOWN*1.5)
        # hm = Text('4').move_to(LEFT*0.5)

        # p = MathTex(r'P=2a+c').move_to(RIGHT*3+UP).set_color(GOLD_C)
        # # p2 = MathTex(r'\overline{P}=\frac{a+b+c}{2}').set_color(RED).move_to(RIGHT*3.5+DOWN*1.2)
        # S = MathTex(r'S=\frac{1}{2}ah_{a}').move_to(RIGHT*3.63).set_color(BLUE_C)
        # Sc = MathTex(r'S=\frac{1}{2}ch_{c}').move_to(RIGHT*3.63).set_color(BLUE_C)
        # Sp = MathTex(r'S=\frac{1}{2}*5*4=10').move_to(RIGHT*3.63).set_color(BLUE_C)
        # self.wait()
        # self.play(Create(p1d),Create(p2d),Create(p3d))
        # self.play(Create(tr))
        # self.wait()
        # self.play(Write(a), Write(b), Write(c))
        # self.wait(2)
        # self.play(Write(p))
        # self.play(Create(l1), Write(h))
        # self.wait(2)

        # self.play(Write(S))
        # self.wait()
        # self.play(ReplacementTransform(S, Sc), FadeIn(tc, shift=LEFT))
        # self.wait(2)
        # self.play(ReplacementTransform(c, cm), ReplacementTransform(h, hm), FadeOut(tc, shift=RIGHT))
        # self.wait()
        # self.play(ReplacementTransform(Sc, Sp))
        # self.wait()
        # self.play(Write(p2))
        # self.wait(2)
        
        
        
        
        
        
        
        # c = Circle(radius=2, color=YELLOW, stroke_width=3)
        # t1 = Text('Шеңбер').move_to(UP*3)
        # l1 = Line(ORIGIN, RIGHT*2, color=GREEN_C)
        # r = Text('r').move_to(RIGHT+UP*0.45)
        # p = MathTex(r'\pi=3.14').move_to(RIGHT*3+UP).set_color(GOLD_C)
        # S = MathTex(r'S=\pi r^2').move_to(RIGHT*3).set_color(RED)
        # l = MathTex(r'C=2\pi r=\pi D').move_to(RIGHT*3.5+DOWN).set_color(BLUE_C)
        # self.wait()
        # self.play(Create(c))
        # self.wait()
        # self.play(Write(t1))
        # self.wait()
        # self.play(Write(l1), Write(r))
        # self.wait()
        # self.play(Write(p))
        # self.wait(2)
        # self.play(Write(S), Write(l))
        # self.wait()
        

    
        
        
        
        # s = Square(side_length=2.0, fill_color=YELLOW, color=YELLOW)
        # t1 = Text('Шаршы', color=GOLD, slant=ITALIC).move_to(UP*1.5)
        # self.wait()
        # self.play(Write(s), s.animate.set_fill(YELLOW, opacity=0.6), Write(t1))
        # self.wait()
        # self.play(Write(NumberPlane()))
        # p1 = np.array([1, 1, 0])
        # p2 = np.array([1, -1, 0])
        # p3 = np.array([-1, -1, 0])
        # p4 = np.array([-1, 1, 0])
        # l1 = Line(p1, p2)
        # l2 = Line(p2, p3)
        # l3 = Line(p3, p4)
        # l4 = Line(p4, p1)
        # square = Polygon(p1, p2, p3, p4, color=GOLD)
        # square.set_fill(GOLD, 0.5)
        # t1 = Text('Шаршы', color=BLUE, slant=ITALIC).move_to(RIGHT*3+UP*1.5)

        # d = Line(np.array([1, 1, 0]), np.array([-1, -1, 0]), color=RED)

        # r1 = Text('a').move_to(LEFT*1.2)
        # r2 = Text('a').move_to(RIGHT*1.2)
        # r3 = Text('a').move_to(UP*1.2)
        # r4 = Text('a').move_to(DOWN*1.2)
        
        # a1 = RightAngle(l1, l2, quadrant=(-1, 1), length=0.4)
        # a2 = RightAngle(l2, l3, quadrant=(-1, 1), length=0.4)
        # a3 = RightAngle(l3, l4, quadrant=(-1, 1), length=0.4)
        # a4 = RightAngle(l4, l1, quadrant=(-1, 1), length=0.4)

        # s = MathTex(r'S=a*a').set_color(YELLOW).move_to(RIGHT*3)
        # s1 = MathTex(r'S=a^2').set_color(YELLOW).move_to(RIGHT*3)

        # p = MathTex(r'P=a+a+a+a').set_color(GREEN).move_to(RIGHT*3+DOWN)
        # p1 = MathTex(r'P=4*a').set_color(GREEN).move_to(RIGHT*3+DOWN)

        # ds = MathTex(r'S=\frac{d^2}{2}').set_color(RED).move_to(RIGHT*3)

        # self.play(DrawBorderThenFill(square), Write(t1))
        # self.wait()
        
        # self.wait()
        # self.play(Create(a1), Create(a2), Create(a3), Create(a4))
        # self.wait()
        # self.play(Write(r1))
        # self.wait()
        # self.play(Write(r2), Write(r3), Write(r4) )
        # self.wait(2)
        # self.play(Write(s))
        # self.wait()
        # self.play(ReplacementTransform(s, s1))
        # self.wait(2)
        # self.play(Write(p))
        # self.wait()
        # self.play(ReplacementTransform(p, p1))
        # self.wait(2)
        
        # self.play(FadeOut(s1, shift=LEFT), FadeOut(p1, shift=RIGHT))
        # self.wait()
        # self.play(Create(d))
        # self.wait()
        # self.play(Write(ds))
        # self.wait()
        
        
        
        
        # r1 = Rectangle(width=4.0, height=3.0, color=GOLD_C)
        # a = Text('4').scale(0.5).move_to(UP*1.67)
        # b = Text('3').scale(0.5).move_to(LEFT*2.2)
        # a1 = Text('4').scale(0.5).move_to(DOWN*1.67)
        # b1 = Text('3').scale(0.5).move_to(RIGHT*2.2)
        # p = Text('P=4+4+3+3=14').scale(0.75)
        # self.wait()
        # self.play(Write(r1), Write(a), Write(b), Write(a1), Write(b1))
        # self.wait(3)
        # self.play(Write(p))
        # self.wait()
        
        # p1 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN, fill_color=GREEN)
        
        # t1 = Text('Жазықтықтағы қандай да бір фигура', color=PURPLE_A).scale(0.6).move_to(UP*1.2)
        # a1 = Arrow(start=(0, 0, 0), end=RIGHT*2, color=GOLD)
        # s = Text('Ауданы S').move_to(RIGHT*3.2)
        # self.wait()
        # self.play(Write(p1), Write(t1))
        # self.wait()
        # self.play(p1.animate.set_fill(GREEN, opacity=0.5), Create(a1), Write(s))
        # self.wait()
        
        
        
        
        
        
        
        
        
        
        
        
        
        # START = (-8,3,0)
        # END =   (8,3,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 2. « Мекеме қызметкерлері жайлы есеп. »', t2c={'Мысал 2': '#ef233c'}).move_to(UP*3.3).scale(0.38)
        # # text2= Text('орман да салынған. Қалғаны түсініксіз суреттер. Қанша түсініксіз суреттер салынған?»', t2c={'1:20000000': YELLOW}).move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), FadeIn(text1, shift=UP))
        # c1 = Circle(radius=1.5).move_to(LEFT*0.75).set_color(YELLOW)
        # c2 = Circle(radius=1.5).move_to(RIGHT*0.75).set_color(YELLOW)
        # c3 = Circle(radius=1.5).move_to(DOWN).set_color(YELLOW)
        # t1 = Text('Ағылшын - 24').scale(0.6)
        # t2 = Text('Неміс - 15').scale(0.6)
        # t3 = Text('Француз - 14').scale(0.6)
        # t4 = Text('Үш тілді де - 3').move_to(UP*2).scale(0.4)
        # t5 = Text('3').move_to(DOWN*0.2)

        # t6 = Text('6 адам ағылшын және неміс тілін біледі').scale(0.4).move_to(UP*2.5).set_color(BLUE_C)
        # t61 = Text('5 адам ағылшын және француз тілін біледі').scale(0.4).move_to(UP*2.5).set_color(BLUE_C)
        # t62 = Text('4 адам неміс және француз тілін біледі').scale(0.4).move_to(UP*2.5).set_color(BLUE_C)

        # t7 = Text('6-3').scale(0.5).move_to(UP*0.7)
        # t71 = Text('5-3').scale(0.5).move_to(DOWN+LEFT)
        # t72 = Text('4-3').scale(0.5).move_to(DOWN+RIGHT)
    
        # t8 = Text('3').move_to(UP*0.81)
        # t81 = Text('2').move_to(DOWN+LEFT)
        # t82 = Text('1').move_to(DOWN+RIGHT)

        
        # g = VGroup(c1, c2, c3)
        # self.wait()
        # self.play(Write(g), Write(t1.next_to(c1, direction=(UP+LEFT))), Write(t2.next_to(c2, direction=(UP+RIGHT))), Write(t3.next_to(c3, direction=DOWN)), Write(t4))
        # self.wait()
        # self.play(ReplacementTransform(t4, t5))
        # self.wait(3)
        # self.play(Write(t6))
        # self.wait()
        # self.play(ReplacementTransform(t6, t7))
        # self.wait()
        # self.play(ReplacementTransform(t7, t8))
        # self.wait()

        # self.play(Write(t61))
        # self.wait()
        # self.play(ReplacementTransform(t61, t71))
        # self.wait()
        # self.play(ReplacementTransform(t71, t81))
        # self.wait()

        # self.play(Write(t62))
        # self.wait()
        # self.play(ReplacementTransform(t62, t72))
        # self.wait()
        # self.play(ReplacementTransform(t72, t82))
        # self.wait(2)
        
        # self.play(t1.animate.set_color(RED).scale(1.1), t8.animate.set_color(RED).scale(1.1), t81.animate.set_color(RED).scale(1.1), t5.animate.set_color(RED).scale(1.1))
        # self.wait()
        
        # t9 = Text('24-(3+3+2)=16').scale(0.4).move_to(UP*2.5).set_color(GREEN)
        # t91 = Text('16').move_to(1.012*LEFT+UP*0.81)
        # self.play(Write(t9))
        # self.wait()
        # self.play(ReplacementTransform(t9, t91))
        # self.wait()




        # self.play(Write(t3))
        # self.wait()
        # self.play(ReplacementTransform(t3, t4))
        # self.wait()
        # self.play(ReplacementTransform(t1,t5), ReplacementTransform(t2,t6))
        # self.wait()
        # self.play(ReplacementTransform(t5, t7), ReplacementTransform(t6,t8))
        # self.wait()
        # self.play(GrowFromCenter(t9))
        # self.wait()
        # self.play(ReplacementTransform(t9, t10))
        # self.wait()
        
        
        
        
        
        
        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 3. «Алматы мен Нұр-Сұлтан қалаларының арасы шамамен 1200 км. Осы арақашықтық бір картада  ', t2c={'Мысал 3': '#ef233c', '1200': YELLOW}).move_to(UP*3).scale(0.38)
        # text2= Text('1:20000000 масштабта сызылған. Картадағы арақашықтығын есептеп тап.»', t2c={'1:20000000': YELLOW}).move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), FadeIn(text1, shift=UP), FadeIn(text2, shift=DOWN))
        # p1 = MathTex(r'mashtab=\frac{1}{20000000}').scale(1.5)
        # p2 = MathTex(r'\frac{1}{20000000}=\frac{x cm}{1200km}')
        # p3 = MathTex(r'\frac{1}{20000000}=\frac{x cm}{120000000cm}')
        # p4 = MathTex(r'x=120000000cm:20000000')
        # p5 = MathTex(r'x=6cm')
        # self.wait()
        # self.play(Write(p1))
        # self.wait()
        # self.play(p1.animate.set_color(YELLOW).scale(1.2))
        # self.wait(2)
        # self.play(ReplacementTransform(p1, p2))
        # self.wait(2)
        # self.play(ReplacementTransform(p2, p3))
        # self.wait(2)
        # self.play(ReplacementTransform(p3, p4))
        # self.wait(2)
        # self.play(ReplacementTransform(p4, p5))
        # self.wait(2)
        



        # self.camera.background_color = GRAY_A
        # text1 = Text('«Екі қаланың арақашықтығы картада 5 сантиметрмен белгіленген. Ал шын өмірде ').move_to(UP*1.5).set_color(BLACK).scale(0.48)
        # text2 = Text('бұл екі қала арасы 150 километр. Осы картаның масштабы неше?»').set_color(BLACK).scale(0.48)
        # # p = MathTex(r'maschtab=\frac{5cm}{150km}=\frac{5cm}{15000000cm}').set_color(BLACK).scale(1.5).move_to(UP*1.7)
        # # p1 = MathTex(r'maschtab=\frac{1}{3000000}').set_color(BLACK).scale(1.35).move_to(DOWN*0.5)
        # # p2 = MathTex(r'maschtab=1:3000000').set_color(BLACK).scale(1.5).move_to(DOWN*2)
        # self.add(text1, text2)




    
        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 1. «Екі қаланың арақашықтығы картада 5 сантиметрмен белгіленген. Ал шын өмірде ', t2c={'Мысал 1': '#ef233c'}).move_to(UP*3).scale(0.38)
        # text2= Text('бұл екі қала арасы 150 километр. Осы картаның масштабы неше?»').move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), FadeIn(text1, shift=UP), FadeIn(text2, shift=DOWN))
        # p1 = MathTex(r'mashtab=\frac{30}{x\%}')
        # p2 = MathTex(r'100*x=30*45')
        # p3 = MathTex(r'x=13.5kg')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # t1 = Text('Мыс массасы белгісіз х').move_to(UP*1.5).scale(0.8).set_color(YELLOW)
        # t2 = Text('Белгісіз мыс пен біздің қоспаны араластырғандағы салмақ: 30+х').move_to(UP*1.5).scale(0.42).set_color(YELLOW)
        # self.wait()
        # self.play(Write(t1))
        # self.wait()
        # self.play(ReplacementTransform(t1, t2))
        # self.wait()
        # self.play(FadeOut(t2, shift=LEFT))
        # k1 = MathTex(r'\frac{30+x}{13.5}=\frac{100\%}{30\%}')
        # k2 = MathTex(r'x=15kg')
        # self.play(Write(k1))
        # self.wait()
        # self.play(ReplacementTransform(k1, k2))
        # self.wait()



        
        
        
        
        
        
        # p1 = MathTex(r'\frac{16}{x}=\frac{100}{30}').move_to(LEFT*2.5)
        # p2 = MathTex(r'100*x=30*16').move_to(LEFT*2.5)
        # p3 = MathTex(r'x=4.8').move_to(LEFT*2.5)
        # k1 = MathTex(r'\frac{9}{x}=\frac{100}{80}').move_to(RIGHT*2.5)
        # k2 = MathTex(r'100*x=9*80').move_to(RIGHT*2.5)
        # k3 = MathTex(r'x=7.2').move_to(RIGHT*2.5)
        # # ans = Text('Жауабы: 20%').scale(0.8).set_color('#588157').move_to(UP*1.7)
        # self.wait()
        # self.play(Write(p1))
        # self.wait()
        # self.play(ReplacementTransform(p1, p2))    
        # self.wait()
        # self.play(ReplacementTransform(p2, p3))
        # self.wait(2)
        # self.play(Write(k1))
        # self.wait()
        # self.play(ReplacementTransform(k1, k2))    
        # self.wait()
        # self.play(ReplacementTransform(k2, k3))
        # self.wait(2)
        # self.play(FadeOut(line1, shift=DOWN), FadeOut(p3, shift=DOWN),FadeOut(k3, shift=DOWN))
        # self.wait(2)
        # j1 = MathTex(r'\frac{16kg+9kg}{4.8kg+7.2kg}=\frac{100\%}{x\%}')
        # j2 = MathTex(r'\frac{25kg}{12kg}=\frac{100\%}{x\%}')
        # j3 = MathTex(r'25*x=12*100')
        # j4 = MathTex(r'x=48\%')
        # self.play(Write(j1))
        # self.wait()
        # self.play(ReplacementTransform(j1, j2))    
        # self.wait()
        # self.play(ReplacementTransform(j2, j3))
        # self.wait()
        # self.play(ReplacementTransform(j3, j4))
        # self.wait(2)






        # self.wait()
        # t2 = MathTex(r'2012^{2021}=...?').set_color(YELLOW)
        # t3 = MathTex(r'2^{2021}=...?').set_color(YELLOW)
        # self.wait()
        # self.play(Write(t2))
        # self.wait()
        # self.play(ReplacementTransform(t2, t3))
        # self.wait()
        # self.play(FadeOut(t3, shift=DOWN))
        # self.wait(3)
        # a1 = MathTex(r'2^1=2')
        # a2 = MathTex(r'2^2=4')
        # a3 = MathTex(r'2^3=8')
        # a4 = MathTex(r'2^4=16')
        # a5 = MathTex(r'2^5=32')
        # a6 = MathTex(r'2^6=64')
        # g = VGroup(a1, a2, a3, a4, a5, a6).arrange(buff=1)
        # self.play(Write(g))
        # self.wait(3)
        # self.play(FadeOut(g, shift=DOWN))
        # self.wait(2)
        # per = Text('Периоды 4 болады.').set_color(GREEN)
        # p1 = MathTex(r'\frac{2021}{4}=505 (1)')
        # p2 = Text('Қалдығы 1 болды. Негізінің осы дәрежесінің мәнін табамыз.').set_color(RED_B).scale(0.5)
        # p3 = MathTex(r'2^1=2')
        # self.play(Write(per))
        # self.wait(3)
        # self.play(ReplacementTransform(per, p1))
        # self.wait(3)
        # self.play(ReplacementTransform(p1, p2))
        # self.wait(3)
        # self.play(ReplacementTransform(p2, p3))
        # self.wait()

        # a1 = MathTex(r'2^1=2')
        # a2 = MathTex(r'2^2=4')
        # a3 = MathTex(r'2^3=8')
        # a4 = MathTex(r'2^4=16')
        # a5 = MathTex(r'2^5=32')
        # a6 = MathTex(r'2^6=64')
        # g = VGroup(a1, a2, a3, a4, a5, a6).arrange(buff=1)
        # self.wait()
        # self.play(Write(g))
        # self.wait()
        
        
        
        
        # self.camera.background_color = GRAY_A
        # text1 = Text('Кері пропорциямен').move_to(UP*3).set_color(BLACK).scale(1.5)
        # p = MathTex(r'\frac{6}{x}=\frac{8}{3}').set_color(BLACK).scale(1.5).move_to(UP*1.7)
        # p1 = MathTex(r'x*3=6*8\Longrightarrow x=\frac{180}{3}').set_color(BLACK).scale(1.35).move_to(UP*0.2)
        # p2 = MathTex(r'x=16').set_color(BLACK).scale(1.5).move_to(DOWN*1.126)
        # self.add(p, p1, p2, text1)
        
        # self.camera.background_color = GRAY_A
        # p = Text('Жаңа логикалық амал ⊚ келесі түрде берілген:').set_color(BLACK).move_to(UP*1.1).scale(0.78)
        # p1 = Text('e⊚f=2e:f. 21⊚7=?').set_color(BLACK).scale(0.78)
        # # p2 = MathTex(r'2(3a+2b)-a+b=?').set_color(BLACK).scale(1.5)
        # self.add(p, p1)
        
        
        
        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 1. «1, 7, 13, 19, ... 12-ші мүшесі нешеге тең?»', t2c={'Мысал 1': '#ef233c'}).move_to(UP*3).scale(0.38)
        # self.wait()
        # self.play(Create(line), FadeIn(text1, shift=UP))
        # self.wait()
        # p = MathTex(r'a_{n}=a_{1}+(n-1)*d').set_color('#ffb703')
        # p1 = MathTex(r'a_{12}=1+(12-1)*6').set_color('#ffb703')
        # p2 = MathTex(r'a_{12}=1+11*6').set_color('#ffb703')
        # p3 = MathTex(r'a_{12}=67').set_color('#ffb703')
        # self.play(Write(p))
        # self.wait()
        # self.play(ReplacementTransform(p, p1))
        # self.wait()
        # self.play(ReplacementTransform(p1, p2))
        # self.wait()
        # self.play(ReplacementTransform(p2, p3))
        # self.wait()


















        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 3. «Асан пирогты 4 минутта, Үсен 6 минутта, Досан 12 минутта жеп бітіреді. ', t2c={'Мысал 3': '#ef233c'}).move_to(UP*3).scale(0.38)
        # text2= Text('Олар үшеуі бірігіп, осы пирогты неше минутта бітіреді? »').move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), FadeIn(text1, shift=UP), FadeIn(text2, shift=DOWN))
        # self.wait()
        # p = MathTex(r'\frac{1}{4}+\frac{1}{6}+\frac{1}{12}=\frac{6}{12}').set_color('#ffb703')#.move_to(LEFT*3.5 + UP)
        # p1 = MathTex(r'\frac{1}{4}+\frac{1}{6}+\frac{1}{12}=\frac{12}{6}').set_color('#ffb703')#.move_to(LEFT*3.5 + UP)
        # p2 = MathTex(r'2 sagat').set_color('#ffb703')#.move_to(LEFT*3.5 + UP)
        # self.play(Write(p))
        # self.wait()
        # self.play(ReplacementTransform(p, p1))
        # self.wait()
        # self.play(ReplacementTransform(p1, p2))
        # self.wait()


        # a1 = MathTex(r'6^1=6')
        # a2 = MathTex(r'6^2=36')
        # a3 = MathTex(r'6^3=216')
        # a4 = MathTex(r'6^2=1296')
        # g = VGroup(a1, a2, a3, a4).arrange(buff=1)
        # self.wait()
        # self.play(Write(g))
        # self.wait()
        
        

        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 3. «Қорапта 20 шар бар. Ішінде 12 ақ, 8 қара шар бар екені белгілі. Қораптың ішіне қарамай, екі шар ', t2c={'Мысал 3': '#ef233c'}).move_to(UP*3).scale(0.38)
        # text2= Text('алған кезде екеуі де қара болуының ықтималдығы неше?»').move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), FadeIn(text1, shift=UP), FadeIn(text2, shift=DOWN))
        # self.wait()
        # p = MathTex(r'P(A,B)= P(A)*P(B) =\frac{m}{n}*\frac{m-1}{n-1}').set_color('#ffb703')#.move_to(LEFT*3.5 + UP)
        # pa = MathTex(r'P(A)=\frac{8}{20}*100=40\%=0.4 ').set_color('#ffb703')#.move_to(LEFT*3.5 + UP)
        # pb = MathTex(r'P(B)=\frac{7}{19}*100=36.8\%=0.368 ').set_color('#ffb703')#.move_to(LEFT*3.5 + UP)
        # pc = MathTex(r'P(A)*P(B)=0.4*0.368=0.147=14.7\%').set_color('#ffb703')
        # self.play(FadeIn(p, shift=UP))
        # self.wait(5)
        # self.play(ReplacementTransform(p, pa))
        # self.wait(2)
        # self.play(ReplacementTransform(pa, pb))
        # self.wait(2)
        # self.play(ReplacementTransform(pb, pc))
        # self.wait(2)



        # p = MathTex(r'P(A)=\frac{m}{n}*100 %').scale(2).set_color('#ffb703')
        # self.wait()
        # self.play(Write(p))
        # self.wait()



        # a1 = MathTex(r'\overline A^m_{n}=n^m').scale(2).set_color('#f72585')
        # a2 = MathTex(r'\overline A^2_{5}=5^2=25').scale(2).set_color('#f72585')
        # self.wait()
        # self.play(Write(a1))
        # self.wait()
        # self.play(ReplacementTransform(a1, a2))
        # self.wait()



        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 1. «’Қазан’ сөзінің ішіндегі әріптерін орындарын ауыстырып неше түрлі сөздер құрастыруға болады? ', t2c={'Мысал 1': '#ef233c'}).move_to(UP*3).scale(0.38)
        # text2= Text('Сөздердің мәні болуы шарт емес.»').move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), Write(text1), Write(text2))
        # self.wait()
        # p1 = MathTex(r'P(n_{1},...,n_{k})=\frac{n!}{n_{1}!*...*n_{k}!}').set_color('#fee440').scale(2)
        # p2 = MathTex(r'P_{5}=\frac{n!}{n_{1}!}').set_color('#fee440').scale(2)
        # p3 = MathTex(r'P_{5}=\frac{5!}{2!}=60').set_color('#fee440').scale(2)
        # self.play(Write(p1))
        # self.wait(2.5)
        # self.play(ReplacementTransform(p1, p2))
        # self.wait(2.5)
        # self.play(ReplacementTransform(p2, p3))
        # self.wait()
        
        
        # c = MathTex(r'C^m_{n}=\frac{n!}{m!(n-m)!}').set_color('#fee440').scale(2)
        # self.wait()
        # self.play(Write(c))
        # self.wait()
        # self.play(FadeOut(c, shift=DOWN))
        # self.wait(2)
        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 1. «Қорапта 4 әр түсті шарлар бар. Ақ, қызыл, көк және жасыл.', t2c={'Мысал 1': '#ef233c'}).move_to(UP*3).scale(0.38)
        # text2= Text('Осы шарлардан неше түрлі жұптар жасауға болады?»').move_to(UP*2.5).scale(0.38)
        # self.wait()
        # self.play(Create(line), Write(text1), Write(text2))
        # self.wait()
        # c_white1 = Circle(radius=0.5, fill_opacity=1, color=WHITE)
        # c_white2 = Circle(radius=0.5, fill_opacity=1, color=WHITE)
        # c_white3 = Circle(radius=0.5, fill_opacity=1, color=WHITE)
        # c_red1 = Circle(radius=0.5, fill_opacity=1, color=RED)
        # c_red2 = Circle(radius=0.5, fill_opacity=1, color=RED)
        # c_red3 = Circle(radius=0.5, fill_opacity=1, color=RED)
        # c_blue1 = Circle(radius=0.5, fill_opacity=1, color=BLUE)
        # c_blue2 = Circle(radius=0.5, fill_opacity=1, color=BLUE)
        # c_blue3 = Circle(radius=0.5, fill_opacity=1, color=BLUE)
        # c_green1 = Circle(radius=0.5, fill_opacity=1, color=GREEN)
        # c_green2 = Circle(radius=0.5, fill_opacity=1, color=GREEN)
        # c_green3 = Circle(radius=0.5, fill_opacity=1, color=GREEN)
        # g1 = VGroup(c_white1, c_red1).arrange(buff=0.3).move_to(LEFT*2+UP*1.3)
        # g2 = VGroup(c_white2, c_blue1).arrange(buff=0.3).move_to(LEFT*2+UP*0.112)
        # g3 = VGroup(c_white3, c_green1).arrange(buff=0.3).move_to(LEFT*2+DOWN*1.26)
        # g4 = VGroup(c_red2, c_blue2).arrange(buff=0.3).move_to(RIGHT*2+UP*1.3)
        # g5 = VGroup(c_red3, c_green2).arrange(buff=0.3).move_to(RIGHT*2+UP*0.112)
        # g6 = VGroup(c_blue3, c_green3).arrange(buff=0.3).move_to(RIGHT*2+DOWN*1.26)

        # self.play(Create(g1), Create(g2), Create(g3), Create(g4), Create(g5), Create(g6))
        # # self.add(g1, g2, g3, g4, g5, g6)
        # self.wait()



        # a = MathTex(r'A^m_{n}=\frac{n!}{(n-m)!}').scale(2).set_color('#fee440')
        # am = MathTex(r'A^2_{5}=\frac{5!}{(5-2)!}').scale(2).set_color('#fee440')
        # am1 = MathTex(r'A^2_{5}=\frac{5!}{3!}').scale(2).set_color('#fee440')
        # am1 = MathTex(r'A^2_{5}=\frac{5!}{3!}=20').scale(2).set_color('#fee440')
        # self.wait()
        # self.play(Write(a))
        # self.wait(8)
        # self.play(ReplacementTransform(a, am))
        # self.wait()
        # self.play(ReplacementTransform(am, am1))
        # self.wait()
        
        
        # t = Text('n! = 1*2*3*...*n').scale(2).set_color('#c1121f')
        # t1 = Text('4! = 1*2*3*4 = 24').scale(2).set_color('#8ac926')   
        # self.wait()
        # self.play(Write(t))
        # self.wait(2)
        # self.play(ReplacementTransform(t, t1))
        # self.wait()


        # c = MathTex(r'C^m_{n}=\frac{n!}{m!(n-m)!}(3)').move_to(LEFT*2+DOWN*1.45).set_color('#dc2f02')
        # a = MathTex(r'A^m_{n}=\frac{n!}{(n-m)!}(2)').move_to(LEFT*2+UP*0.12).set_color('#f72585')
        # p = MathTex(r'P_{n}=n!(1)').move_to(LEFT*3.2+UP*1.3).set_color('#fee440')
        # a1 = MathTex(r'\overline A^m_{n}=n^m').move_to(RIGHT*2+UP*0.12).set_color('#f72585')
        # p1 = MathTex(r'P(n_{1},...,n_{k})=\frac{n!}{n_{1}!*...*n_{k}!}').move_to(RIGHT*3.65+UP*1.3).set_color('#fee440')
        # t = Text('Негізгі формулалар')
        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('КОМБИНАТОРИКА', color=RED_C).move_to(UP*3).scale(0.68)
        # self.wait()
        # self.play(Create(line), Write(text1))
        # self.wait()
        # self.play(Write(c), Write(a), Write(p), Write(a1), Write(p1))
        # self.wait()
        


        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 2. «1, 2, 3, 4, 5 цифрлар көмегімен неше екі таңбалы сан құрастыруға болады? Цифрлар қайталанбауы керек.»', t2c={'Мысал 2': '#ef233c'}).move_to(UP*3).scale(0.38)
        # self.wait()
        # self.play(Create(line), Write(text1))
        # self.wait()
        # nums = array([[12, 13, 14, 15], [21, 23, 24, 25],
        #             [31, 32, 34, 35], [41, 42, 43, 45], [51, 52, 53, 54]])
        # table = IntegerTable(nums, include_outer_lines=False).scale(0.69).move_to(DOWN).set_color('#0081a7')
        # self.play(Create(table))
        # self.wait()      
        # t = Text('Барлығы: 20 сан.').move_to(RIGHT*4.3).scale(0.6)
        # self.play(Write(t))



        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # text1 = Text('Мысал 1. «A, B, C әріптерін орындарын ауыстырып, неше түрлі әріптер комбинацияларын алуға болады?»', t2c={'Мысал 1': '#ef233c'}).move_to(UP*3).scale(0.38)
        # self.wait()
        # self.play(Create(line), Write(text1))
        # self.wait()
        # abc = Text('A B C', color='#2a9d8f').move_to(LEFT*2+UP*1.3)
        # acb = Text('A C B', color='#d62828').move_to(LEFT*2+UP*0.39)
        # bca = Text('B C A', color='#f77f00').move_to(LEFT*2+DOWN*0.65)
        # bac = Text('B A C', color='#8ecae6').move_to(RIGHT*2+UP*1.3)
        # cba = Text('C B A', color='#edf2f4').move_to(RIGHT*2+UP*0.39)
        # cab = Text('C A B', color='#ff9b54').move_to(RIGHT*2+DOWN*0.65)
        # self.play(Write(abc), Write(acb), Write(bca), Write(bac), Write(cba), Write(cab))
        # self.wait()



        # text1 = Text('«Мысал 2. Катер 2 сағат ішінде өзен ағысына қарсы 120 километр қашықтықты жүзіп өтті.', t2c={'Мысал 2': '#ef233c',
        #                                                                                                            'өзен ағысына қарсы':'#fca311'}).move_to(UP*3).scale(0.38)
        # text2= Text('Егер өзен ағысының жылдамдығы 5 км/сағ болса, онда катердің жылдамдығын тап. »').move_to(UP*2.5).scale(0.38)
        # START = (-8,2,0)
        # END =   (8,2,0)
        # line = Line(START,END);
        # self.wait()
        # self.play(Create(line), Write(text1), Write(text2))
        # self.wait(2)
        # #vm = MathTex(r'\vartheta_{m}=40 km/sag').move_to(LEFT*4 + UP*1.5)
        # S = MathTex(r'S=120 km').move_to(LEFT*4 + UP*1.5)
        # vo = MathTex(r'\vartheta_{\theta}=5 km/sag').move_to(LEFT*4 + UP*0.688)
        # t = MathTex(r't=2 sag').move_to(LEFT*4)
        # vm = MathTex(r'\vartheta_{m}=?').move_to(LEFT*4 + DOWN)
        # self.play(Write(S))
        # self.wait()
        # self.play(Write(vo))
        # self.wait()
        # self.play(Write(t))
        # self.wait()
        # self.play(Write(vm))
        # self.wait()
        # v1 = MathTex(r'\vartheta_{m}-\vartheta_{\theta}=\frac{s}{t}', color='#006d77').move_to(RIGHT*1.5+UP*1.200).scale(1.8)
        # v2 = MathTex(r'\vartheta_{m}=\frac{s}{t}+\vartheta_{\theta}', color='#006d77').move_to(RIGHT*1.5+UP*1.200).scale(1.8)
        # self.play(Write(v1))
        # self.wait()
        # self.play(ReplacementTransform(v1, v2))
        # self.wait()
        # ta = MathTex(r'\vartheta_{m}=\frac{120}{2}+5 = 65 km/sag').move_to(RIGHT*1.5+DOWN*0.366)
        # ans = Text('Жауабы: 65 км/сағ.').move_to(RIGHT*1.5+DOWN*1.366)
        # self.wait()
        # self.play(Write(ta))
        # self.wait()
        # self.play(Write(ans))
        # self.wait()



        # v = MathTex(r'\vartheta=\frac{s}{t}', color='#cdb4db').move_to(3.5*LEFT).scale(2)
        # s = MathTex(r's=\vartheta t', color='#ffbe0b').scale(2)
        # t = MathTex(r't=\frac{s}{\vartheta}', color='#e63946').move_to(3.5*RIGHT).scale(2)
        # v1 = MathTex(r'\vartheta_{m}\pm\vartheta_{\theta}=\frac{s}{t}', color='#cdb4db').move_to(2.5*UP).scale(2)
        # s1 = MathTex(r's=(\vartheta_{m}\pm\vartheta_{\theta}) t', color='#ffbe0b').scale(2)
        # t1 = MathTex(r't=\frac{s}{(\vartheta_{m}\pm\vartheta_{\theta})}', color='#e63946').move_to(2.5*DOWN).scale(2)
        # self.wait()
        # self.play(Write(v), Write(s), Write(t))
        # self.wait(8)
        # self.play(ReplacementTransform(v, v1), ReplacementTransform(s, s1), ReplacementTransform(t, t1))
        # self.wait()
               
               
        
        # axes = ThreeDAxes()
        # cylinder = Cylinder(radius=2, height=3)
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.wait()
        # self.play(Create(axes), Create(cylinder))
        # self.wait()      
        
        

        # f = Text('Функция y=x-5').scale(2).set_color('#8ac926')
        # t1 = Text('1. y(6) = 6-5 = 1').scale(2).set_color('#8ac926')
        # t2 = Text('2. y(7)-y(5) = (7-5)-(5-5) = 2').scale(1.68).set_color('#8ac926')
        # t3 = Text('3. y(15) = 15-5 = 10').scale(2).set_color('#8ac926')
        # self.play(Write(f))
        # self.wait()
        # self.play(ReplacementTransform(f, t1))
        # self.wait()
        # self.play(ReplacementTransform(t1, t2))
        # self.wait()
        # self.play(ReplacementTransform(t2, t3))
        # self.wait()
               
        
        
        # self.camera.background_color = GRAY_A
        # task = Text('1.	y = x – 5 функциясы берілген.', color='#252422')
        # ques = Text('y(6), y(7) – y(5), y(15) анықта.', color='#252422').move_to(DOWN*1.5)
        # self.wait()
        # self.play(Write(task), Write(ques))
        # self.wait()

        
        
        #div = MathTex(r"y=\frac{5}{2x+6}").scale(3).set_color('#588157')
        # log = MathTex(r'y=\log_2 (2(x-5))').scale(2).set_color('#8ac926')
        # con = MathTex(r'2(x-5)> 0').scale(2).set_color('#8ac926')
        # con1 = MathTex(r'x-5>0').scale(2).set_color('#8ac926')
        # con2 = MathTex(r'x>5').scale(2).set_color('#8ac926')
        # self.play(Write(log))
        # self.wait()
        # self.play(ReplacementTransform(log, con))
        # self.wait()
        # self.play(ReplacementTransform(con, con1))
        # self.wait()
        # self.play(ReplacementTransform(con1, con2))
        # self.wait()
        # answer = Text('Жауабы: ').move_to(LEFT * 5)
        # ans = MathTex(r'x\in(5; +\infty)').scale(1.28).set_color('#8ac926')
        # self.play(ReplacementTransform(con2, ans), Write(answer))
        # self.wait()



        # sq = MathTex(r'y = \sqrt{x}').scale(3).set_color('#2a9d8f')
        # div = MathTex(r"y=\frac{1}{x}").scale(3).set_color('#588157')
        # log = MathTex(r'y=\log_2 x').scale(3).set_color('#ffbe0b')        
        # self.wait()
        # self.play(Write(sq))
        # self.wait()
        # self.play(ReplacementTransform(sq, div))
        # self.wait()
        # self.play(ReplacementTransform(div, log))
        # self.wait()
        
        
        
        # a = Axes(
        #      x_range=[-6, 6],
        #      y_range=[-8, 8],
        #      y_length=9,
        #      x_length=15,
        #      axis_config={
        #          "include_numbers": True,
        #          },
        #          ).scale(0.7)
        # one = Text('1-ші ширек').move_to(RIGHT * 3 + UP * 3).set_color(BLUE)
        # two = Text('2-ші ширек').move_to(LEFT * 3 + UP * 3).set_color(GREEN)
        # three = Text('3-ші ширек').move_to(LEFT * 3 + DOWN * 3).set_color(RED)
        # four = Text('4-ші ширек').move_to(RIGHT * 3 + DOWN * 3).set_color(YELLOW_A)
        # self.wait()
        # self.play(Write(a), Write(one), Write(two), Write(three), Write(four))
        # self.wait()        
        
        
        
        # a = Axes(
        #     x_range=[-6, 6],
        #     y_range=[-8, 8],
        #     y_length=9,
        #     x_length=15,
        #     axis_config={
        #         "include_numbers": True,
        #         },
        #         ).scale(0.7)
        # self.wait()
        # self.play(Write(a))
        # labels = a.get_axis_labels(x_label='x', y_label='y').set_color(BLUE)
        # x_vals = linspace(-2,2,5)
        # y_vals = [f(i) for i in x_vals]
        # t1 = DecimalTable(
        #     [x_vals, y_vals],
        #     row_labels=[MathTex("x"), MathTex("f(x)")],
        #     include_outer_lines=True).move_to(LEFT * 3.7 + UP * 2).scale(0.45)
        # self.play(Write(labels))
        # self.wait(2)
        # self.play(Write(t1))
        # self.wait(2)
        # for i in range(len(x_vals)):
        #     l = [(x_vals[i], y_vals[i])]
        #     dot_axes = Dot(a.coords_to_point(l), color=GREEN)
        #     lines = a.get_lines_to_point(a.c2p(l))
        #     self.play(Create(dot_axes), Create(lines))
        # self.wait(2)
        # graph = a.plot(lambda x: 2*(x-2), color=BLUE)
        # label_for_graph = a.get_graph_label(graph, label='y = 2(x-2)')
        # self.play(Create(graph), Write(label_for_graph))
        # self.wait()
        


        
        # text = MathTex("y", "=", "f", " (", "x", ")")
        # f_name = Text('Функцияның аты', gradient=(BLUE, GREEN), color=BLUE_C).move_to(DOWN * 2).scale(2)
        # x_text = Text('Функция аргументі', gradient=(BLUE, GREEN), color=BLUE_C).move_to(DOWN * 2).scale(2)
        # f = SurroundingRectangle(text[2], buff=.1, color=GREEN_A).scale(3)
        # x = SurroundingRectangle(text[5], buff=.1, color=GREEN_A).scale(3)
        # self.wait()
        # self.play(Write(text.scale(3)))
        # self.wait()
        # self.play(Create(f))
        # self.play(Write(f_name))
        # self.wait()
        # self.remove(f)
        # self.remove(f_name)
        # self.wait()
        # self.play(Create(x.move_to(RIGHT * 1.88)))
        # self.play(Write(x_text))
        # self.wait()