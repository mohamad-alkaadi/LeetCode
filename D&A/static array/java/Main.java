public class Main{
    public static void main(String[] args){
        StaticArray staticArray = new StaticArray();
        int[] arrayOne = new int[4];
        arrayOne[0] = 1;
        arrayOne[1] = 2;
        arrayOne[2] = 3;

        arrayOne = staticArray.insertEnd(arrayOne, 9, 3, 4);
        System.out.println(arrayOne[2]);
    }
}