namespace learn
{
    using System;
    public class DivideyVenceras()
    {

        public void IntroduccionunA�o()
        {
            Console.WriteLine("Ingrese un a�o:");
            string year = Console.ReadLine();

            int yearint = Int32.Parse(year);

            bool isLearpYear = EsVissiesto(yearint);
        }
        private bool EsVissiesto(int date)

        {
            if(date % 4 == 0)
            {
                if(date % 100 == 0)
                {
                    if(date % 400 == 0)
                    {
                        Console.WriteLine("la fecha " + date + "es visiesto");
                        return true;
                    }
                }
            }
            else
            {
                Console.WriteLine("El a�o no es visiesto");
            }
            
            return false;
        }

    }



}