package java;

public class quickSort{
    public static void main(){
        int[] arr = {3,1,124,6,2,532,3421};
        quickSort1(arr);
    }        

    public static void quickSort1(int[] arr){
        quickSort2(arr, 0, arr.length-1);
    }

    private static void swap(int[] arr, int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    private static void quickSort2(int[] arr, int start, int end){
        if(start>end){
            return;
        }

        int pivot = arr[start];
        int low = start+1;
        int high = end;

        while(low <= high){
            while(low <= end && arr[low] <= pivot){
                low++;
            }

            while(high > start && arr[high] >= pivot){
                high--;
            }

            if(low > high){
                swap(arr, high, pivot);
            }else{
                swap(arr, low, high);
            }
        }

        quickSort2(arr, start, high-1);
        quickSort2(arr, high+1, end);
    }
}
