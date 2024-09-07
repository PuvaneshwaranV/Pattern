import java.util.Scanner;
class hallowdiamond
{
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		int n=10;
		for(int i=0;i<n;i++)
		{
			int k=n-i+1;int l=0;
			for(int j=0;j<=k;j++)
			{
				System.out.print(" ");
			}
			for(int j=0;j<=i;j++)
			{
				if(j==0 && i!=0)
					System.out.print("* ");
				if(j==0 && i==0)
					System.out.print(" *");
				while(l<(2*i))
				{
					System.out.print(" ");l++;
				}
				if(j==i && i!=0)
				System.out.print("*");
			}
			System.out.println("\n");
		}
		for(int i=n-2;i>-1 ;i--)
		{
			int k=n-i+1;int l=0;
			for(int j=0;j<=k ;j++)
			{
				System.out.print(" ");
			}
			for(int j=0;j<=i;j++)
			{
				if(j==0 && i!=0)
					System.out.print("* ");
				if(j==0 && i==0)
					System.out.print(" *");
				while(l<(2*i))
				{
					System.out.print(" ");l++;
				}
				if(j==i-1)
				System.out.print("*");

			}
			System.out.println("\n");
		}

	}
}