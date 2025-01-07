#ifndef _PROCESSING_H_
#define _PROCESSING_H_

#include "dyn_survey.h"

void compute_conditions_one( int conditions[], Respondent *respondents, int num_respondents );

void compute_conditions_two( int conditions[], Respondent *responses, int num_responses );

void compute_conditions_three( int conditions[], Respondent *responses, int num_responses );

void compute_frequencies( double frequencies[][NUMBER_RESPONSES], int num_questions, Respondent *responses, int num_respondents, int num_likert_levels );

void compute_scores( double scores[][NUMBER_SCORES], Respondent *responses, int num_respondents );

void compute_average_scores( double average_scores[], double scores[][NUMBER_SCORES], int used, int num_respondents );

int responses_used( Respondent *responses, int num_responses );

double compute_c( Respondent *response, int u );

double compute_i( Respondent *response, int u );

double compute_g( Respondent *response, int u );

double compute_u( Respondent *response, int u );

double compute_p( Respondent *response, int u );

#endif
