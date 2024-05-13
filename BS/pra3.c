/*5 pipes*/
#include<stdio.h>
#include<string.h>
int main()
{
int n;
char buff[1024];
int flag[2];
char *data="hello how are you?";
pipe(flag);
write(flag[1],data,strlen(data));
n=read(flag[0],buff,1024);
int i;
for(i=0;i<strlen(buff);i++)
{
printf("%c",buff[i]);
}
printf("\n");
return 0;
}

/*6 character count*/
#include <stdio.h>
#include <string.h>

int main()
{
char s[1000],c;

int i,count=0;

printf("Enter the string : ");
gets(s);
printf("Enter character to be searched: ");
c=getchar();

for(i=0;s[i];i++)
{
if(s[i]==c)
{
count++;
}
}

printf("character '%c' occurs %d times \n ",c,count);

return 0;
}

/*7 bit count*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
int x[20],y[30],i,j,k,count,n;
printf("Enter the frame length: ");

scanf("%d",&n);
printf("Enter the input frame (0's & 1's only): ");
for(i=0;i<n;i++)
scanf("%d",&x[i]);
i=0; count=1; j=0;
while(i<n)
{
if(x[i]==1)
{
y[j]=x[i];
for(k=i+1;x[k]==1 && k {
j++;
y[j]=x[k];
count++;
if(count==5)
{
j++;
y[j]=0;
}
i=k;
}}
else
{
y[j]=x[i];
}
i++;
j++;
}
printf("After stuffing the frame is: ");

for(i=0;i<j;i++)
printf("%d",x[i]);
getch();
}

/*8 GNU C generate frames from sender’s message by
splitting message by given frame-length.*/
#include <stdio.h>
#include <string.h>

// Function to generate frames from sender's message
void generateFrames(const char *message, int frameLength) {
int messageLength = strlen(message);
int numFrames = messageLength / frameLength;
if (messageLength % frameLength != 0)
numFrames++;

printf("Number of frames: %d\n", numFrames);

int i, j;
for (i = 0; i < numFrames; i++) {
printf("Frame %d: ", i + 1);
for (j = 0; j < frameLength && i * frameLength + j < messageLength; j++) {
printf("%c", message[i * frameLength + j]);
}
printf("\n");
}
}

int main() {

const char *message = "This is a test message for frame generation.";
int frameLength = 10;

printf("Original message: %s\n", message);
printf("Frame length: %d\n", frameLength);

generateFrames(message, frameLength);

return 0;
}

/*9 byte stuffing*/
#include <stdio.h>
#include <string.h>

#define FLAG_BYTE 0x7E
#define STUFF_BYTE 0x7D
#define ESCAPE_BYTE 0x20 // XOR with this to get stuffed byte

// Function to stuff bytes in a frame
void byteStuffing(const unsigned char *data, int length) {
printf("Sender's Original Frame: ");
putchar(FLAG_BYTE);
for (int i = 0; i < length; i++) {
if (data[i] == FLAG_BYTE || data[i] == STUFF_BYTE) {
putchar(STUFF_BYTE);
putchar(data[i] ^ ESCAPE_BYTE);
} else {
putchar(data[i]);
}

}
putchar(FLAG_BYTE);
printf("\n");
}

int main() {
// Sender's data
const unsigned char data[] = {0x11, 0x7E, 0x7D, 0x31, 0x20, 0x7D};

// Calculate length of data
int length = sizeof(data) / sizeof(data[0]);

// Perform byte stuffing
byteStuffing(data, length);

return 0;
}

/*10 bit stuffing*/
#include <stdio.h>

#define FLAG_BYTE 0x7E
#define STUFF_BYTE 0x7D
#define ESCAPE_BYTE 0x20 // XOR with this to get stuffed byte
#define MAX_DATA_LENGTH 100

// Function to perform bit stuffing
void bitStuffing(const unsigned char *data, int length) {
printf("Sender's Original Frame: ");
putchar(FLAG_BYTE);

int count = 0;
for (int i = 0; i < length; i++) {
if (data[i] == FLAG_BYTE) {
putchar(STUFF_BYTE);
putchar(data[i] ^ ESCAPE_BYTE);
count = 0;
} else {
putchar(data[i]);
if (data[i] == STUFF_BYTE) {
count++;
if (count == 5) {
putchar(STUFF_BYTE);
putchar(0x5E); // Escape sequence for STUFF_BYTE
count = 0;
}
} else {
count = 0;
}
}
}

putchar(FLAG_BYTE);
printf("\n");
}

int main() {
// Sender's data
const unsigned char data[] = {0x11, 0x7E, 0x7D, 0x31, 0x7D, 0x7D, 0x7D};

// Calculate length of data
int length = sizeof(data) / sizeof(data[0]);

// Perform bit stuffing
bitStuffing(data, length);

return 0;
}

/*11 LRC */
#include &lt;stdio.h&gt;
// Function to calculate LRC
unsigned char calculateLRC(unsigned char *data, int length) {
unsigned char lrc = 0;
for (int i = 0; i &lt; length; i++) {
lrc += data[i];
}
// Take the one&#39;s complement of the sum
lrc = (~lrc) + 1;
return lrc;
}
// Function to print a byte in binary format
void printBinary(unsigned char byte) {
for (int i = 7; i &gt;= 0; i--) {
printf(&quot;%d&quot;, (byte &gt;&gt; i) &amp; 1);
}
}
int main() {
// Example data to be sent (replace this with your actual data)
unsigned char dataToSend[] = {0x41, 0x42, 0x43, 0x44}; // &quot;ABCD&quot; in ASCII
int dataLength = sizeof(dataToSend) / sizeof(dataToSend[0]);
// Calculate LRC for the data
unsigned char lrc = calculateLRC(dataToSend, dataLength);

// Append LRC to the data
dataToSend[dataLength] = lrc;
// Display the data with appended LRC in binary format
printf(&quot;Data with appended LRC (in binary):\n&quot;);
for (int i = 0; i &lt; dataLength + 1; i++) {
printBinary(dataToSend[i]);
printf(&quot; &quot;);
}
printf(&quot;\n&quot;);
return 0;
}

/* 11 Checksum*/
#include&lt;stdio.h&gt;
#include&lt;math.h&gt;
int sender(int arr[10],int n)
{
int checksum,sum=0,i;
printf(&quot;\n***SENDER SIDE*\n&quot;);
for(i=0;i&lt;n;i++)
sum+=arr[i];
printf(&quot;SUM IS: %d&quot;,sum);
checksum=~sum; //1&#39;s complement of sum
printf(&quot;\nCHECKSUM IS:%d&quot;,checksum);
return checksum;
}
void receiver(int arr[10],int n,int sch)
{
int checksum,sum=0,i;
printf(&quot;\n\n***RECEIVER SIDE*\n&quot;);
for(i=0;i&lt;n;i++)
sum+=arr[i];
printf(&quot;SUM IS:%d&quot;,sum);
sum=sum+sch;
checksum=~sum; //1&#39;s complement of sum
printf(&quot;\nCHECKSUM IS:%d&quot;,checksum);

}
void main()
{
int n,sch,rch;
printf(&quot;\nENTER SIZE OF THE STRING:&quot;);
scanf(&quot;%d&quot;,&amp;n);
int arr[n];
printf(&quot;ENTER THE ELEMENTS OF THE ARRAY TO CALCULATE CHECKSUM:\n&quot;);
for(int i=0;i&lt;n;i++)
{
scanf(&quot;%d&quot;,&amp;arr[i]);
}
sch=sender(arr,n);
receiver(arr,n,sch);
}

/* 12 CRC*/

#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
#define N strlen(gen_poly)
char data[28];
char check_value[28];
char gen_poly[10];
int data_length,i,j;
void XOR(){
for(j = 1;j &lt; N; j++)
check_value[j] = (( check_value[j] == gen_poly[j])?&#39;0&#39;:&#39;1&#39;);
}
void receiver(){
// get the received data
printf(&quot;Enter the received data: &quot;);
scanf(&quot;%s&quot;, data);
printf(&quot;\n-----------------------------\n&quot;);
printf(&quot;Data received: %s&quot;, data);
crc();
for(i=0;(i&lt;N-1) &amp;&amp; (check_value[i]!=&#39;1&#39;);i++);
if(i&lt;N-1)
printf(&quot;\nError detected\n\n&quot;);
else
printf(&quot;\nNo error detected\n\n&quot;);
}
void crc(){
// initializing check_value

for(i=0;i&lt;N;i++)
check_value[i]=data[i];
do{
if(check_value[0]==&#39;1&#39;)
XOR();
for(j=0;j&lt;N-1;j++)
check_value[j]=check_value[j+1];
// appending a bit from data
check_value[j]=data[i++];
}while(i&lt;=data_length+N-1);
// loop until the data ends
}
int main()
{
printf(&quot;\nEnter data to be transmitted: &quot;);
scanf(&quot;%s&quot;,data);
printf(&quot;\n Enter the Generating polynomial: &quot;);
scanf(&quot;%s&quot;,gen_poly);
data_length=strlen(data);
for(i=data_length;i&lt;data_length+N-1;i++)
data[i]=&#39;0&#39;;
printf(&quot;\n----------------------------------------&quot;);
printf(&quot;\n Data padded with n-1 zeros : %s&quot;,data);
printf(&quot;\n----------------------------------------&quot;);
crc();
printf(&quot;\nCRC or Check value is : %s&quot;,check_value);
for(i=data_length;i&lt;data_length+N-1;i++)
data[i]=check_value[i-data_length];
printf(&quot;\n----------------------------------------&quot;);
printf(&quot;\n Final data to be sent : %s&quot;,data);
printf(&quot;\n----------------------------------------\n&quot;);

receiver();
return 0;
}

/*13 Hamming Code*/
#include &lt;stdio.h&gt;
#include &lt;math.h&gt;
int input[32];
int code[32];
int ham_calc(int,int);
void main()
{
int n,i,p_n = 0,c_l,j,k;
printf(&quot;Please enter the length of the Data Word: &quot;);

scanf(&quot;%d&quot;,&amp;n);
printf(&quot;Please enter the Data Word:\n&quot;);
for(i=0;i&lt;n;i++)
{
scanf(&quot;%d&quot;,&amp;input[i]);
}
i=0;
while(n&gt;(int)pow(2,i)-(i+1))
{
p_n++;
i++;
}
c_l = p_n + n;
j=k=0;
for(i=0;i&lt;c_l;i++)
{
if(i==((int)pow(2,k)-1))
{
code[i]=0;
k++;
}
else
{
code[i]=input[j];
j++;
}
}
for(i=0;i&lt;p_n;i++)
{
int position = (int)pow(2,i);
int value = ham_calc(position,c_l);
code[position-1]=value;
}
printf(&quot;\nThe calculated Code Word is: &quot;);
for(i=0;i&lt;c_l;i++)
printf(&quot;%d&quot;,code[i]);
printf(&quot;\n&quot;);
printf(&quot;Please enter the received Code Word:\n&quot;);
for(i=0;i&lt;c_l;i++)
scanf(&quot;%d&quot;,&amp;code[i]);

int error_pos = 0;
for(i=0;i&lt;p_n;i++)
{
int position = (int)pow(2,i);
int value = ham_calc(position,c_l);
if(value != 0)
error_pos+=position;

}
if(error_pos == 1)
printf(&quot;The received Code Word is correct.\n&quot;);
else
printf(&quot;Error at bit position: %d\n&quot;,error_pos);

}
int ham_calc(int position,int c_l)
{
int count=0,i,j;
i=position-1;
while(i&lt;c_l)
{
for(j=i;j&lt;i+position;j++)
{
if(code[j] == 1)
count++;

}
i=i+2*position;
}
if(count%2 == 0)
return 0;
else
return 1;

}

/*14 Leaky Bucket*/
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt; // For sleep function
int main() {
int i, packets[10], content = 0, newcontent, time, clk, bucket_size, output_rate;
// Generate random packet sizes
for (i = 0; i &lt; 5; i++) {

packets[i] = rand() % 10;
if (packets[i] == 0)
i--; // Regenerate if packet size is 0
}
printf(&quot;\nEnter output rate of the bucket: &quot;);
scanf(&quot;%d&quot;, &amp;output_rate);
printf(&quot;\nEnter Bucket size: &quot;);
scanf(&quot;%d&quot;, &amp;bucket_size);
for (i = 0; i &lt; 5; ++i) {
if ((packets[i] + content) &gt; bucket_size) {
if (packets[i] &gt; bucket_size)
printf(&quot;\nIncoming packet size %d greater than the size of the bucket\n&quot;,
packets[i]);
else
printf(&quot;\nBucket size exceeded\n&quot;);
} else {
newcontent = packets[i];
content += newcontent;
printf(&quot;\nIncoming Packet: %d\n&quot;, newcontent);
printf(&quot;Transmission left: %d\n&quot;, content);
time = rand() % 10;
printf(&quot;Next packet will come at: %d\n&quot;, time);
for (clk = 0; clk &lt; time &amp;&amp; content &gt; 0; ++clk) {
printf(&quot;\nLeft time: %d&quot;, (time - clk));
sleep(1);
if (content &gt; 0) {
printf(&quot;\nTransmitted\n&quot;);
if (content &lt; output_rate)
content = 0;
else
content -= output_rate;
printf(&quot;Bytes remaining: %d\n&quot;, content);

} else {
printf(&quot;\nNo packets to send\n&quot;);
}
}
}
}
return 0;
}

/*15 Token Bucket*/
#include &lt;stdio.h&gt;
#include &lt;stdbool.h&gt;
#include &lt;unistd.h&gt; // for usleep function
int main() {
int bucket_size, output_rate;
printf(&quot;Enter the bucket size: &quot;);
scanf(&quot;%d&quot;, &amp;bucket_size);
printf(&quot;Enter the output rate of the bucket: &quot;);
scanf(&quot;%d&quot;, &amp;output_rate);
int bucket = 0; // Current size of the bucket
while (true) {
int incoming_packets;
printf(&quot;Enter the number of incoming packets: &quot;);
scanf(&quot;%d&quot;, &amp;incoming_packets);
// Add incoming packets to the bucket
if (bucket + incoming_packets &lt;= bucket_size) {
bucket += incoming_packets;
} else {
printf(&quot;Bucket overflow! Dropping %d packets.\n&quot;, incoming_packets +
bucket - bucket_size);
bucket = bucket_size;
}
// Transmit data from the bucket
if (bucket &gt;= output_rate) {
printf(&quot;%d packets transmitted.\n&quot;, output_rate);
bucket -= output_rate;
} else {

printf(&quot;Bucket empty.\n&quot;);
}
usleep(1000000);
}
return 0;
}