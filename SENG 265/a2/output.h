#ifndef _OUTPUT_H_
#define _OUTPUT_H_

#include "dyn_survey.h"

void print_output( short *test, int num_tests,
		char **questions, int num_questions,
		char **likert_level, int num_likert_levels,
		Respondent *responses, int num_respondents,
		double frequencies[][NUMBER_RESPONSES], double scores[][NUMBER_SCORES],
		double average_scores[], int used );

#endif
