#ifndef _DYN_SURVEY_H_
#define _DYN_SURVEY_H_

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define NUMBER_SCORES 5
#define NUMBER_QUESTIONS 38
#define NUMBER_RESPONSES 6
#define MAX_LINE_LENGTH 3000

typedef struct Responses {
	int ans;
	double wight;
} Responses;

typedef struct Respondent {
	char *name;
	int canadian;
	int age;
	int on_or_off;
	Responses responses[38];
} Respondent;



#endif
