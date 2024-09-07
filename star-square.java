import java.util.Scanner;
class starsquare
{
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		int n=11;
		int[][] a=new int[n][n];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(i==0 || i==n-1 || j==n-1 || j==0 ||i==j || i+j==n-1)
					System.out.print("*");
				else
					System.out.print(" ");
			}
			System.out.print("\n");
		}
	}
}