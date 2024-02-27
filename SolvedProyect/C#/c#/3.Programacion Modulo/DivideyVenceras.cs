namespace learn
{
    using System;
    public class DivideyVenceras()
    {
        
        public void IntroduccirUnA�o()
        {
            
            Console.Write("Ingrese su nombre: ");
            string year = Console.ReadLine();

            int yearint = Int32.Parse(year);

            bool isLeapYear = EsVisiesto(yearint);


            // Mostrar el resultado
            if (isLeapYear)
            {
                Console.WriteLine("El a�o {0} es bisiesto", yearint);
            }
            else
            {
                Console.WriteLine("El a�o {0} no es bisiesto", yearint);
            }

        }
        private bool EsVisiesto(int date)
        {
                if(date % 4 == 0) 
                {
                    if(date % 100 == 0) 
                    { 
                        if (date % 400 == 0) 
                        {
                            return true;
                        }
                    }
                }
                return false;
        }


     }


}