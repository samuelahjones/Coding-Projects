#include "processing.h"

void compute_conditions_one( int conditions[], Respondent *respondents, int num_respondents ) {
	if( conditions[0] != 0 ) {
		if( conditions[0] == 1 ) {
			for( int i = 0; i < num_respondents; i++ ) {
				if( strcmp(respondents[i].name, "Engineering") == 0 ) {
					respondents[i].on_or_off = 1;
				} else { 
					respondents[i].on_or_off = 0;
				}
			}
		} else if( conditions[0] == 2 ) {
			for( int i = 0; i < num_respondents; i++ ) {
				if( strcmp(respondents[i].name, "Health") == 0 ) {
					respondents[i].on_or_off = 1;
				} else {
					respondents[i].on_or_off = 0;
				}
			}
		} else {
			for( int i = 0; i < num_respondents; i++ ) {
				if( strcmp(respondents[i].name, "Art") == 0 ) {
					respondents[i].on_or_off = 1;
				} else {
					respondents[i].on_or_off = 0;
				}
			}
		}
	}
}


void compute_conditions_two( int conditions[], Respondent *responses, int num_responses ) {
	if( conditions[1] != 0 ) {
		if( conditions[1] == 1 ) {
			for( int i = 0; i < num_responses; i++ ) {
				if( responses[i].canadian == 1 && responses[i].on_or_off == 1 ) {
					responses[i].on_or_off = 1;
				} else {
					responses[i].on_or_off = 0;
				}
			}
		} else { 
			for( int i = 0; i < num_responses; i++ ) {
				if( responses[i].canadian == 0 ) {
					responses[i].on_or_off = 1;
				} else {
					responses[i].on_or_off = 0;
				}
			}
		}
	}
}


void compute_conditions_three( int conditions[], Respondent *responses, int num_responses ) {
	if( conditions[3] != 0 ) {
		for( int i = 0; i < num_responses; i++ ) {
			if( responses[i].age >= conditions[2] && responses[i].age <= conditions[3] ) {
				responses[i].on_or_off = 1;
			} else {
				responses[i].on_or_off = 0;
			}
		}
	}
}


void compute_frequencies( double frequencies[][NUMBER_RESPONSES], int num_questions, Respondent *responses, int num_respondents, int num_likert_levels ) {
	for( int i = 0; i < num_questions; i++ ) {
		double counted = 0;
		for( int j = 0; j < num_respondents; j++ ) {
			if( responses[j].on_or_off == 1 ) {
				counted++;
				int g = responses[j].responses[i].ans - 1;
				frequencies[i][g]++;
			}

		}
		for( int k = 0; k < num_likert_levels; k++ ) {
			frequencies[i][k] = 100.0 * frequencies[i][k] / counted;
		}
	}
	return;
}


void compute_scores( double scores[][NUMBER_SCORES], Respondent *responses, int num_respondents ) {
	for( int i = 0; i < num_respondents; i++ ) {
		scores[i][0] = compute_c(responses, i);
		scores[i][1] = compute_i(responses, i);
		scores[i][2] = compute_g(responses, i);
		scores[i][3] = compute_u(responses, i);
		scores[i][4] = compute_p(responses, i);
	}
	return;
}

void compute_average_scores( double average_scores[], double scores[][NUMBER_SCORES], int used, int num_respondents ) {
	for( int i = 0; i < NUMBER_SCORES; i++ ) {
		average_scores[i] = 0.0;
		for( int j = 0; j < num_respondents; j++ ) {
			average_scores[i] += scores[j][i]; 
		}
		if( num_respondents > 0 ) {
			average_scores[i] /= ((double)used);
		}
	}
	return;
}

int responses_used( Respondent *responses, int num_responses ) {
	int used = 0;
	for( int i = 0; i < num_responses; i++ ) {
		if( responses[i].on_or_off == 1 ) {
			used++;
		}
	}
	return used;
}

double compute_c( Respondent *response, int u ) {
	double sum = 0;
	for( int i = 0; i <= 7; i++ ) {
		if( response[u].on_or_off == 1 ) {
			sum += response[u].responses[i].wight;
		}
	}
	return sum / 8.0;
}

double compute_i( Respondent *response, int u ) {
	double sum = 0;
	for( int i = 8; i <= 17; i++ ) {
		if( response[u].on_or_off == 1 ) {
			sum += response[u].responses[i].wight;
		}
	}
	return sum / 10.0;
}

double compute_g( Respondent *response, int u ) {
	double sum = 0;
	for( int i = 18; i <= 27; i++ ) {
		if( response[u].on_or_off == 1 ) {
			sum += response[u].responses[i].wight;
		}
	}
	return sum / 10.0;
}

double compute_u( Respondent *response, int u ) {
	double sum = 0;
	for( int i = 28; i <= 33; i++ ) {
		if( response[u].on_or_off == 1 ) {
			sum += response[u].responses[i].wight;
		}
	}
	return sum / 6.0;
}

double compute_p( Respondent *response, int u ) {
	double sum = 0;
	for( int i = 34; i <=37; i++ ) {
		if( response[u].on_or_off == 1 ) {
			sum += response[u].responses[i].wight;
		}
	}
	return sum / 4.0;
}

