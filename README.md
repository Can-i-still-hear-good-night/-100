import java.util.Scanner;

public class zhekou {
    public static void main(String[] args) {
        int Tx = 539;
        int xie = 888;
        int pai = 159;
        System.out.println("请输入折扣(1~9):");
        Scanner jv = new Scanner(System.in);
        int zhi = jv.nextInt();
        switch (zhi) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:

                double jia = Tx*zhi/10;
                double xz = xie*zhi/10;
                double pz = pai*zhi/10;

                if (jia<=100||xz<=100||pz<=100){
                    boolean f=jia<100;
                    boolean ff=xz<100;
                    boolean fff=pz<100;

                    System.out.println("T恤的价格折扣完低于100吗？"+f);
                    System.out.println("T恤"+zhi+"折后的价格是"+jia);
                    System.out.println("鞋子的价格折扣完低于100吗？"+ff);
                    System.out.println("鞋子"+zhi+"折后的价格是"+xz);
                    System.out.println("拍子的价格折扣完低于100吗？"+fff);
                    System.out.println("拍子"+zhi+"折后的价格是"+pz);
                }
                else {
                    System.out.println("所有物品"+zhi+"折后的价格都高于100元");
                    System.out.println("拍子"+zhi+"折后的价格是"+pz);
                    System.out.println("鞋子"+zhi+"折后的价格是"+xz);
                    System.out.println("T恤"+zhi+"折后的价格是"+jia);
                }
            break;
            default:
                System.out.println("请正确输入折扣");
        }
    }
}
