namespace learn
{
    using System;
    public class DivideyVenceras()
    {
        
        public void IntroducirAño()
        {
            
            Console.Write("Ingrese su nombre: ");
            string year = Console.ReadLine();

            int yearint = Int32.Parse(year);

            bool isLeapYear = EsVisiesto(yearint);


            // Mostrar el resultado
            if (isLeapYear)
            {
                Console.WriteLine("El año {0} es bisiesto", yearint);
            }
            else
            {
                Console.WriteLine("El año {0} no es bisiesto", yearint);
            }

        }
        private bool  EsBisiesto(int date)
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
					else
					{
						return true;
					}
                }
				
                return false;
        }


     }


}