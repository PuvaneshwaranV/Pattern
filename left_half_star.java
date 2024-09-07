import java.util.Scanner;
class left_half_star
{
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		int n=5;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(!(i<=j))
				System.out.print("*");
			}
			System.out.print("\n");
		}
	}
}