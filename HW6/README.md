HW 6
===
Dijkstra 介紹
---
指定一個點 (源點) 到其餘各個頂點的最短路徑，也稱作「單源最短路徑」。  

- 做法:  
1.設定一個初始全部為空(False)的list(seen)，當前頂點若已經走過，則改成True。  
2.設定另一個各個位置初始皆為無限大(99999)的list，代表與被選擇的點的距離(dis[])。被選擇的起始點與自己的距離為0。  
3.以助教的圖為例: 起點為0
0可以連到點1和7，距離分別為4和8(dis[1]=4, dis[7]=8)。接著先取距離較近的點1，可以走到點2和7。  
此時0到2的距離從無限大(非相鄰)修改成較近的4+8=12(dis[2]=dis[1]+g.graph[1][2]);0到7的距離維持不變(因為8<4+11)。  
4.將已走訪的點index，在list seen中的False修改為True。  
5.重複以上動作，直到所有點皆看過(seen == [True] * self.V)。


Kruskal 介紹
---
1.把邊照權重大小排序。  
2.將點到點的邊連出，但樹不能有loop(一顆生成樹只能有一個root)。
.當某條邊的兩端點不存在於同一顆生成樹時 → 留下這條邊且root會改變  
.當某條邊的兩端點存在於同一顆生成樹時，會產生loop → 捨棄這條邊

- 參考資料:https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/  
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
