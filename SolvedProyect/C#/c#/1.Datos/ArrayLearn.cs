

namespace learn
{
  
    public class ArrayLearn()
    {
        private int[] array_number = new int[] { 0, 1, 2, 3, 4, 5 }; 
        
        public void arrayMostrar()
        {
            for(int i = 0; i<= array_number.Length -1 ; i++)
            {  
                Console.WriteLine(array_number[i]);
            }
        }
    }
}


