# **LoRa Technology Combined with ECC for encryption**

### Check out lora-ecc-analysis branch to see progress of our work - [link](https://github.com/tanmayidev/lora-ecc/tree/lora-ecc/analysis)

## **Definitions:**
* **LoRa** (Long Range) is a spread spectrum modulation technique derived from chirp spread spectrum (CSS) technology. Semtech's LoRa is a long range, low power wireless platform that has become the de facto wireless platform of Internet of Things (IoT).

* **ECC** (Elliptic Curve Cryptography) is an approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields. ECC allows smaller keys compared to non-EC cryptography (based on plain Galois fields) to provide equivalent security.

## **Final Goal:**
1. Implement ECC based encryption/decryption for LoRa based systems(coin-cell devices)

2. Make a visualizer for demonstrating its advantages to potential clients.

3. (Maybe) publish a paper on our findings, if the outcomes are feasible enough.

## **Need for ECC?**           

|  KEY SIZE (in bits) 	|  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GENERATION TIME (seconds) 	|
|:-------------------:	|:--------------------------:	|
| **ECC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RSA**  	| **ECC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RSA**   	|
| 163&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1024   | 0.08&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.16     |
| 233&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2240   | 0.18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.47     |
| 283&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3072   | 0.27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.89     |
| 409&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7680   | 0.64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;133.90   |
| 571&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15360  | 1.44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;679.06   |

## **Currently Used Cryptography Algorithms in IoT:**
* AES
* DES
* Triple-DES
* RSA
* DSA
* BlowFish
* TwoFish

## **Spectrum of Elliptic Curves:**
* Hessian curves
* Edwards curves
* Twisted curves
* Twisted Hessian curves
* Twisted Edwards curve
* Doubling-oriented Doche–Icart–Kohel curve
* Tripling-oriented Doche–Icart–Kohel curve
* Jacobian curve
* Montgomery curves

## **Assignment 1:**
1. Find the most suitable algorithm from the Spectrum of Elliptic Curves for IoT devices (Lowest possible computing power required)

2. Simulate algorithm shortlisted from the above step. In C, C++, Python.

3. Simulate (i.e., find time to encrypt and decrypt the message) currently used algorithms in IoT; in C, C++, Python.

4. Simulate the respective algorithms on the following systems :
    - Intel x86/x64
    - ARM Cortex-A72
    - ESP 32
    - M1 (Apple/Mac)

5. Collect performance samples from above simulations and make appropriate stats.
