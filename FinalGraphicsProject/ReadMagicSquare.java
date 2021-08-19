import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Fileto2darray {

    /**
     * @param args
     * @throws IOException 
     */
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        File file = new File("yourfilename.txt");
        FileReader fr = new FileReader(file);
        char temparr[] = new char[(int) file.length()];
        fr.read(temparr,0,(int) file.length());
        String [] tempstring = (new String(temparr)).split("\n");
        String array2d[][] = new String [tempstring.length][];
        for(int i=0 ; i<tempstring.length; i++)
        {
            array2d[i]=tempstring[i].split(", ");               
        }

    }

}