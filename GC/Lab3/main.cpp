// #include <iostream>
// #include <cstdio>
// #include <vector>

// using namespace std;

// struct Punct {
//     float x, y;
//     Punct(float x, float y) : x(x), y(y) {};
//     Punct() {};
// };

// struct Dreapta {
//     int a, b, c;
//     Dreapta(int a, int b, int c) : a(a), b(b), c(c) {};
// };

// void read(vector<Punct> &v) {
//     int x, y;
//     for(int i=0; i<4; i++) {
//         scanf("%d %d",&x,&y);
//         v.push_back(Punct(x, y));
//     }
// }

// Dreapta computeSegment(Punct A, Punct B) {
//     int a, b, c;

//     a = B.y - A.y;
//     b = A.x - B.x;
//     c = A.x*A.y + A.y*B.x - A.x*B.y - A.x*A.y;

//     return Dreapta(a, b, c);
// }

// int linesIntersection(Dreapta d1, Dreapta d2, Punct &p) {
//     int detA = (d1.a*d2.b - d1.b*d2.a);

//     if(detA != 0) {
//         float x = (float)(d2.c*d1.b - d1.c*d2.b) / (d1.a*d2.b - d2.a*d1.b);
//         float y = (float)( -d1.c - d1.a*x) / d1.b;
//         p = Punct(x, y);

//         return 0; /// intersectia intr-un punct
//     } else {
//         int detAb = (d1.b*d2.c - d1.c*d2.b);
//         if(detAb == 0) detAb = (d1.a*d2.c - d1.c*d2.a);

//         if(detAb==2) return -1; /// multimea vida
//     }

//     return 1; ///dreptele coincid
// }

// bool pointOnSegment(Punct A, Punct B, Punct p) {
//     if(A.x <= p.x && B.x >= p.x &&
//        A.y <= p.y && B.y >= p.y)
//         return true;

//     if(A.x >= p.x && B.x <= p.x &&
//        A.y >= p.y && B.y <= p.y)
//         return true;

//     return false;
// }

// bool uniqueSolution() {
//     return true;
// }

// bool segmentsIntersection(Punct A, Punct B, Punct C, Punct D) {
//     Punct st, dr;

//     if(A.x < C.x)
// }

// int main()
// {
//     vector<Punct> puncte;

//     freopen("data.in", "r", stdin);
//     read(puncte);

//     Dreapta d1 = computeSegment(puncte[0], puncte[1]);
//     Dreapta d2 = computeSegment(puncte[2], puncte[3]);

//     Punct p;
//     int err = linesIntersection(d1, d2, p);

//     if(err == 0) {
//         if(pointOnSegment(puncte[0], puncte[1], p) && pointOnSegment(puncte[2], puncte[3], p))
//             printf("Intersectia e un punct: (%.2f, %.2f)\n", p.x, p.y);
//         else
//             printf("Multimea vida!");
//     } else if(err == 1) {


//     }
// }

#include <bits/stdc++.h>

using namespace std;

ifstream in("date.in");

int main() {
	pair< int, int > p1;
	pair< int, int > p2;
	pair< int, int > p3;
	pair< int, int > p4;

	in >> p1.first >> p1.second;
	in >> p2.first >> p2.second;
	in >> p3.first >> p3.second;
	in >> p4.first >> p4.second;

	double a1 = p1.second - p2.second;
	double b1 = p2.first - p1.first;
	double c1 = p1.first * p2.second - p2.first * p1.second;

	double a2 = p3.second - p4.second;
	double b2 = p4.first - p3.first;
	double c2 = p3.first * p4.second - p4.first * p3.second;

	double delta = a1 * b2 - a2 * b1;

	if(delta != 0.0) {
		double x = (((-c1) * b2) - ((-c2) * b1)) / delta;
		double y = ((a1 * (-c2)) - (a2 * (-c1))) / delta;

		int minX1 = min(p1.first, p2.first);
		int maxX1 = max(p1.first, p2.first);
		int minY1 = min(p1.second, p2.second);
		int maxY1 = max(p1.second, p2.second);

		int minX2 = min(p3.first, p4.first);
		int maxX2 = max(p3.first, p4.first);
		int minY2 = min(p3.second, p4.second);
		int maxY2 = max(p3.second, p4.second);

		if(minX1 <= x && x <= maxX1 && minX2 <= x && x <= maxX2 && minY1 <= y && y <= maxY1 && minY2 <= y && y <= maxY2) {
			cout << "Intersectia este: (" << x << ", " << y << ")\n";
		} else {
			cout << "Intersectia este multimea vida!\n";
		}

		return 0;
	}

	if(((-c1) * b2) - ((-c2) * b1) != 0 || (a1 * (-c2)) - (a2 * (-c1)) != 0) {
		cout << "Intersectia este multiema vida!\n";
		return 0;
	} else {
		vector< pair< int, int > > v1(2), v2(2);
		v1[0] = p1; v1[1] = p2; sort(v1.begin(), v1.end());
		v2[0] = p3; v2[1] = p4; sort(v2.begin(), v2.end());

		if(v1[1] < v2[0]) {
			cout << "Intersectia este multimea vida!\n";
			return 0;
		}

		if(v2[1] < v1[0]) {
			cout << "Intersectia este multimea vida!\n";
			return 0;
		}

		if(v1[0] <= v2[0] && v1[1] >= v2[1]) {
			cout << "Intersectia este: (" << v2[0].first << ", " << v2[0].second << "), (" << v2[1].first << ", " << v2[1].second << ")\n";
			return 0;
		} 
		if (v2[0] <= v1[0] && v2[1] >= v1[1]) {
			cout << "Intersectia este: (" << v1[0].first << ", " << v1[0].second << "), (" << v1[1].first << ", " << v1[1].second << ")\n";
			return 0;
		}

		cout << "Intersectia este: (";
		cout << max(v1[0], v2[0]).first << ", " << max(v1[0], v2[0]).second << "), (" << min(v1[1], v2[1]).first << "," << min(v1[1], v2[1]).second << ")\n";
	}

	return 0;
}