// This neural network was originally written in Python (https://www.sololearn.com/learn/738/?ref=app). I converted it to C to deepen my understanding of both languages, as well as of neural networks.

// This neural network recognizes a pattern. If the 1st number in the set is 1, then the output is 1.



#include <stdlib.h> 
#include <stdio.h>
#include <math.h> // M_E



// global variables
int i, num_weights = 3, num_inputs = 3;
double weight[3];

// function prototypes
double sigmoid(double x);
double derivative(double x);
double think(double x, double y, double z);
void train(int iterations);

// training data
int inputs[3][3] = {{1, 1, 1}, {1, 0, 1}, {0, 1, 1}};
int outputs[3] = {1, 1, 0};



int main() {


 
// Seed the pseudo-random number generator with the Process ID. No, this is not the best method. But, it works for this exercise.
srand((unsigned int)getpid()); 



// Generate random weights.
for (i=0; i<num_weights; i++){
    weight[i] = 2*(((double)rand())/RAND_MAX)-1;
    printf("weight%i %f\n", i, weight[i]);
    }



// Train the model using the training data.
train(10000);



// Test the model with new inputs.
printf("test %f\n", think(1, 0, 0));



    return 0;
}



// function definitions

// the Sigmoid normalizes weights between 0 and 1; it is graphed as an S-shaped curve
double sigmoid(double x){
    return (1 / (1 + exp(-x)));
}

// indicates confidence in weights; Gradient Descent: lower confidence results in larger adjustments and zero values do not cause changes
double derivative(double x){
    return (x * (1 - x));
}

double result;
double think(double x, double y, double z){
    result = (sigmoid((x * weight[0]) + (y * weight[1]) + (z * weight[2])));
    return(result);
} 
        
void train(int iterations) {
    int j, k;
    double thought, error, adjustment;
    for (i=0; i<iterations; i++){
        for (j=0; j<num_inputs; j++){
            thought = think(inputs[j][0], inputs[j][1], inputs[j][2]); 
            error = (outputs[j] - thought);
            for (k=0; k<num_inputs; k++){
            adjustment = (inputs[j][k] * error * derivative(thought));
            weight[k] += adjustment;
            }
        }
        if (i % 500 == 0) {
            printf("i %i error %f\n", i, error);
            for (k=0; k<num_weights; k++){
                printf("weight%i %f\n", k, weight[k]);
            }
            printf("\n");
        }
    }
}
