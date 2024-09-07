import java.util.Scanner;
class star
{
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		int n=10;
		for(int i=0;i<n;i++)
		{
			int k=n-i+1;
			for(int j=0;j<=k;j++)
			{
				System.out.print(" ");
			}
			for(int j=0;j<=i;j++)
			{
				System.out.print("* ");
			}
			System.out.println("\n");
		}
		for(int i=n-1;i>-1 ;i--)
		{
			int k=n-i+1;
			for(int j=0;j<=k;j++)
			{
				System.out.print(" ");
			}
			for(int j=0;j<i;j++)
			{
				
				System.out.print(" *");
			}
			System.out.println("\n");
		}

	}
}