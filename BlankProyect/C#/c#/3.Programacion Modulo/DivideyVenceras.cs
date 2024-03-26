namespace learn
{
    using System;
    public class DivideyVenceras()
    {

        public void IntroducirA�o()
        {
            Console.Write("Ingrese su Anio: ");
            string year = Console.ReadLine();
            int yearint = Int32.Parse(year);
            bool IsLeapYear = IsBisiesto(yearint);
            if (IsLeapYear)
            {
                Console.WriteLine("El a�o es {0} es Bisiesto", year);
               
            }
            else
            {
                Console.WriteLine("El A�o {0} no es Bisiesto", year);
            }
            

        }

        private bool IsBisiesto(int date)
        {

            if (date % 4 == 0)
            {
                if (date % 100 == 0)
                {
                    if (date % 400 == 0)
                    {
                        Console.WriteLine("es Bisiesto");
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