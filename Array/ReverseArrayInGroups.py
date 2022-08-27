# void reverseInGroups(ArrayList<Integer> arr, int n, int k) {
#     // code here
#     int lastSize = n%k;
#     int lastMidPoint = lastSize/2;
#
#     int back = k-1;
#     int front = 0;
#     if (k >= n){
#         k = n-1;
#         back = k;
#     }
#         int mid_point = k/2;
#
#         int swapelement1 = 0;
#         int swapelement2 = 0;
#
#
#         while (front < n - lastMidPoint){
#             if (front>back){
#                 front = front + mid_point;
#                 if (k%2==0){
#                     back += k + mid_point;
#                 }else{
#                 back = front + mid_point+1;}
#                 continue;
#             }
#             if (back > n-1 ){
#                 back = n-1;
#                 continue;
#             }
#             swapelement1 = arr.get(front);
#             swapelement2 = arr.get(back);
#             arr.set(front,swapelement2);
#             arr.set(back,swapelement1);
#             back--;
#             front++;
#             if (back == front ){
#                 front = front + mid_point+1;
#                 back += k + mid_point;
#             }
#         }
# }}