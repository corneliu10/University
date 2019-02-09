// GC2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

// Ai (xi, yi) din R^2, i=1,4 distincte 2 cate 2
// Sa se determ multimile I, J a.i:
//	 I U J = {A1, A2, A3, A4}
//   I intersectat J = (-)
//   conv(I) inter conv(J) != (-)
//   patrulater: I={A1, A2} J={A3, A4}
//   triunghi:	 I={A1, A2, A3} J={A4}
//	 segment:    I={A2, A3} J={A1, A4}

#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

#define POINTS_SIZE 3
#define Epsilon		0.001

using namespace std;

typedef struct Point {
	int x, y;
};

bool comparePoints(Point a, Point b) {
	if(a.x < b.x) return 0;
	else if(a.x > b.x) return 1;

	return a.y < b.y;
}

void readPoint(Point &p) {
	scanf("%d %d", &p.x, &p.y);
}

int verifyColiniarityHorizontal(Point x, Point y) {
	return x.x == y.x;
}

int verifyColiniarityVertical(Point x, Point y) {
	return x.y == y.y;
}

void printPointVector(vector<Point> v) {
	for(int i=0; i<v.size(); ++i) {
		printf("(%d, %d) ",v[i].x, v[i].y);
	}
}

float areaOfTriangle(Point a, Point b, Point c) {
	float area;
	area = (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2.0;

	return fabs(area);
}

int verifyTriangleCase(Point p1, Point p2, Point p3, Point p4) {
	float A1 = areaOfTriangle(p1, p2, p3);
	float A2 = areaOfTriangle(p1, p2, p4);
	float A3 = areaOfTriangle(p1, p3, p4);
	float A4 = areaOfTriangle(p4, p2, p3);

	if((A1+A2+A3) - A4 < Epsilon) return 1;
	return 0;
}

void printSets(vector<Point> I, vector<Point> J) {
	printf("I={ ");
	printPointVector(I);
	printf("}\n");

	printf("J={ ");
	printPointVector(J);
	printf("}\n");
}

int main()
{
	Point points[POINTS_SIZE];
	vector<Point> I, J;

    freopen("data.in", "r", stdin);
	readPoint(points[0]);
	readPoint(points[1]);
	readPoint(points[2]);
	readPoint(points[3]);

	int horColiniarity=1, verColiniarity=1;

	for(int i=1; i<POINTS_SIZE; ++i) {
		horColiniarity &= verifyColiniarityHorizontal(points[i], points[i-1]);
		verColiniarity &= verifyColiniarityVertical(points[i], points[i-1]);
	}

	if(verColiniarity || horColiniarity) {
		I.push_back(points[1]);
		I.push_back(points[2]);
		J.push_back(points[0]);
		J.push_back(points[3]);

		printSets(I, J);

		exit(0);
	}

	int triangleCase = 0;

	triangleCase |= verifyTriangleCase(points[0], points[1], points[2], points[3]);
	if(triangleCase) {
		I.push_back(points[1]);
		I.push_back(points[2]);
		I.push_back(points[3]);
		J.push_back(points[0]);

		printSets(I, J);
		exit(0);
	}
	triangleCase |= verifyTriangleCase(points[1], points[0], points[2], points[3]);
	if(triangleCase) {
		I.push_back(points[0]);
		I.push_back(points[2]);
		I.push_back(points[3]);
		J.push_back(points[1]);

		printSets(I, J);
		exit(0);
	}
	triangleCase |= verifyTriangleCase(points[2], points[1], points[0], points[3]);
	if(triangleCase) {
		I.push_back(points[0]);
		I.push_back(points[1]);
		I.push_back(points[3]);
		J.push_back(points[2]);

		printSets(I, J);
		exit(0);
	}
	triangleCase |= verifyTriangleCase(points[3], points[1], points[2], points[0]);
	if(triangleCase) {
		I.push_back(points[0]);
		I.push_back(points[2]);
		I.push_back(points[1]);
		J.push_back(points[3]);

		printSets(I, J);
		exit(0);
	}

    sort(points, points + POINTS_SIZE, comparePoints);
	// patrulater case
	I.push_back(points[0]);
	I.push_back(points[2]);
	J.push_back(points[1]);
	J.push_back(points[3]);

	printSets(I, J);
	exit(0);

	return 0;
}
