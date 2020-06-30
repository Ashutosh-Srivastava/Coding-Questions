// This was my solution submitted and passed all the test cases
/*
Author: Shivansh Bajpai
Java SE8 solution
*/

static int[] solve(int area){
  int count=0;
  int ar[]=new int[area];
  while(area>=1){
    int nl=(int)Math.sqrt(area);
    System.out.println(nl*nl);
    area=area-nl*nl;
    ar[count++]=nl*nl;
  }
  int arl[]=new int[count];
  for(int i =0;i<count;i++)
    arl[i]=ar[i];
  return arl;
}
