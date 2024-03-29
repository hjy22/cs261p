import requirements
import random as rand

def fib_heap_tests():
    fib = requirements.FibHeap()
    
    n3=fib.insert(805910)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    n1 =fib.insert(109533)
    fib.decrease_priority(n1,35325)
    n2=fib.insert(572581)
    fib.decrease_priority(n2,527207)
    fib.decrease_priority(n3,734041)
    fib.insert(250898)
    n5=fib.insert(561558)
    fib.insert(557204)
    fib.delete_min_lazy()
    n4=fib.insert(258327)
    fib.decrease_priority(n4,28581)
    fib.decrease_priority(n5,96177)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(355137)
    fib.insert(166962)
    n6=fib.insert(514868)
    fib.delete_min_lazy()
    n7=fib.insert(910845)
    fib.decrease_priority(n6,47613)
    fib.insert(278177)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n7,698193)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(218735)
    fib.insert(315604)
    fib.insert(217968)
    n13=fib.insert(885180)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    n8=fib.insert(626946)
    fib.insert(134636)
    fib.insert(158222)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(501008)
    n11=fib.insert(806597)
    n10=fib.insert(784603)
    fib.insert(648213)
    fib.insert(827082)
    fib.decrease_priority(n8,600997)
    fib.insert(106677)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(747478)
    n9=fib.insert(850909)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n9,41089)
    fib.insert(828953)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.insert(57907)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    n12=fib.insert(794976)
    fib.decrease_priority(n10,519639)
    fib.delete_min_lazy()
    fib.insert(672116)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n11,544887)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n12,410705)
    fib.insert(420885)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(479979)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n13,401420)
    fib.insert(372538)
    fib.insert(18170)
    n14=fib.insert(958020)
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    n18=fib.insert(779319)
    fib.insert(274903)
    fib.insert(351601)
    fib.decrease_priority(n14,245907)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(241212)
    n15=fib.insert(586701)
    fib.insert(252646)
    fib.insert(679477)
    n16=fib.insert(897542)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    n19=fib.insert(707630)
    fib.decrease_priority(n15,386017)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(50917)
    fib.insert(669055)
    n17=fib.insert(477884)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(142800)
    fib.insert(82440)
    fib.delete_min_lazy()
    fib.insert(320460)
    n22=fib.insert(799971)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n16,210965)
    fib.decrease_priority(n17,75212)
    n20=fib.insert(487128)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n18,744387)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n19,234415)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(193083)
    fib.delete_min_lazy()
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    n23=fib.insert(979882)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    n21=fib.insert(889214)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.decrease_priority(n20,375086)
    fib.find_min()
    print([x.val for x in fib.get_roots()])
    fib.insert(253695)
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(21766)
    fib.decrease_priority(n21,568379)
    fib.find_min()
    fib.decrease_priority(n22,537631)
    fib.delete_min_lazy()
    fib.find_min()
    fib.decrease_priority(n23,43018)
    n24=fib.insert(757265)
    fib.decrease_priority(n24,118716)
    fib.insert(276127)
    fib.delete_min_lazy()
    fib.insert(545179)
    fib.delete_min_lazy()
    fib.find_min()
    n25=fib.insert(39331)
    fib.insert(278481)
    fib.decrease_priority(n25,27316)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(517365)
    fib.find_min()
    fib.delete_min_lazy()
    fib.insert(705105)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(287048)
    n27=fib.insert(787518)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(20690)
    n26=fib.insert(856491)
    fib.decrease_priority(n26,783209)
    fib.delete_min_lazy()
    fib.find_min()
    fib.find_min()
    fib.find_min()
    fib.insert(375988)
    fib.find_min()
    fib.decrease_priority(n27,650410)
    fib.insert(86041)
    fib.insert(880497)
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    fib.delete_min_lazy()
    fib.find_min()
    n28=fib.insert(143551)
    fib.insert(582827)
    fib.insert(138185)
    n31=fib.insert(958222)
    fib.delete_min_lazy()
    fib.find_min()
    fib.decrease_priority(n28,72521)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(307589)
    fib.insert(31716)
    fib.delete_min_lazy()
    fib.find_min()
    fib.find_min()
    fib.insert(113714)
    fib.insert(275296)
    n29=fib.insert(543967)
    fib.insert(944248)
    fib.insert(252986)
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    fib.delete_min_lazy()
    fib.find_min()
    fib.find_min()
    fib.find_min()
    fib.insert(510538)
    fib.delete_min_lazy()
    fib.decrease_priority(n29,479879)
    fib.insert(727506)
    n30=fib.insert(929745)
    fib.decrease_priority(n30,552567)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(742621)
    fib.insert(247642)
    fib.delete_min_lazy()
    fib.find_min()
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(30026)
    fib.insert(11348)
    fib.find_min()
    fib.insert(296017)
    fib.find_min()
    fib.insert(47640)
    fib.find_min()
    fib.find_min()
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    n32=fib.insert(987106)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(373600)
    fib.find_min()
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(935306)
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(747451)
    fib.find_min()
    fib.decrease_priority(n31,1048)
    fib.find_min()
    fib.delete_min_lazy()
    fib.insert(942782)
    fib.find_min()
    fib.insert(363015)
    fib.delete_min_lazy()
    fib.insert(363497)
    fib.find_min()
    fib.find_min()
    fib.find_min()
    fib.insert(265869)
    fib.insert(488591)
    fib.insert(320232)
    fib.find_min()
    fib.find_min()
    fib.delete_min_lazy()
    fib.delete_min_lazy()
    fib.find_min()
    fib.find_min()
    fib.delete_min_lazy()
    fib.insert(344189)
    fib.delete_min_lazy()
    fib.find_min()
    fib.delete_min_lazy()
    fib.find_min()
    fib.insert(547377)
    n34=fib.insert(954011)
    n33=fib.insert(59342)
    fib.insert(941160)
    fib.decrease_priority(n32,67409)
    fib.find_min()
    fib.find_min()
    fib.find_min()
    fib.decrease_priority(n33,56318)
    fib.insert(903988)
    fib.insert(705040)
    fib.delete_min_lazy()
    fib.decrease_priority(n34,820333)
    fib.delete_min_lazy()
    fib.find_min()

    
    print("done!")

if __name__ == '__main__':
	fib_heap_tests()