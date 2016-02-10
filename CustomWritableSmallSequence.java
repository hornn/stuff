


import org.apache.hadoop.util.StringUtils;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.io.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.compress.*;
import org.apache.hadoop.mapreduce.lib.output.*;

import java.net.URI;
import java.net.URISyntaxException;



import java.io.IOException;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.DataOutputStream;
import java.io.DataInputStream;
import java.io.OutputStream;
import java.io.InputStream;
import java.io.EOFException;
import java.util.Calendar;

import java.sql.Timestamp;
import java.util.Date;
import java.text.SimpleDateFormat;

import org.apache.hadoop.io.Writable;

import com.pivotal.pxf.hadoop.io.GPDBWritable;




public class CustomWritableSmallSequence 
{
	private Configuration conf;
	
	private String        outPath;
	private String        outFile;
	
	private String        fullPath;
	private boolean       doPrint;
	static private int           do_write; // 1 - Write, 0 - read
	private int 	      rowsNumber;	
	
	public CustomWritableSmallSequence(String[] args) 
	{
		conf        = new Configuration();
		conf.set("fs.default.name", "hdfs://localhost/");
		
		outPath     = args[0];
		outFile     = args[1];
		do_write    = Integer.parseInt(args[2]);
		if (do_write == 1)
			rowsNumber  = Integer.parseInt(args[3]);
		doPrint     = true;
		
		URI outputURI = null;
		try 
		{
			outputURI = new URI(outPath);
		} catch (URISyntaxException e) 
		{
		}
		
		fullPath = outputURI.getPath() + Path.SEPARATOR + outFile;
		System.out.println(fullPath);
	}
	
	void WriteFile()
	{
		System.out.println("WriteFile");
		
		FileSystem fs = null;
		try 
		{
			fs = FileSystem.get(URI.create(fullPath), conf);
		
			IntWritable key = new IntWritable();
			CustomWritableSmall val = new CustomWritableSmall();
			Path path = new Path(outPath + Path.SEPARATOR + outFile);
			SequenceFile.Writer writer = SequenceFile.createWriter(fs, conf, path, key.getClass(), val.getClass());
			
			for (int i=1; i<=rowsNumber; i++)
			{
				int num1 = i;
				
				CustomWritableSmall cust = new CustomWritableSmall(num1, 10*num1, 20*num1);
				//if (i == 1)
					//cust.SetErrMode(false);
				
				writer.append(key, cust);
			}
			
			IOUtils.closeStream(writer);
		}
		catch (java.io.IOException ie)
		{
		}
	}
	
	void printField(String fld)
	{
		if (doPrint)
			System.out.println(fld);
	}
	
	void ReadFile()
	{
		System.out.println("ReadFile\n");
		
		FileSystem fs = null;
		FSDataInputStream inp = null;
		try 
		{
			fs = FileSystem.get(URI.create(fullPath), conf);
			Path p = new Path(outPath + Path.SEPARATOR + outFile);
			
			SequenceFile.Reader reader = new SequenceFile.Reader(fs, p, conf);
			IntWritable key = (IntWritable)ReflectionUtils.newInstance(reader.getKeyClass(), conf);
			CustomWritableSmall cust = (CustomWritableSmall)ReflectionUtils.newInstance(reader.getValueClass(), conf);
			
			System.out.println("The class field types are:");
			cust.printFieldTypes();
			System.out.println("\n\n");
			
			SimpleDateFormat form = new SimpleDateFormat("EEE dd MMM yyyy HH:mm:ss.SSS");
			Date z = new Date();
			System.out.println(form.format(z).toString());
			
			try
			{
				int sizo = 1000;
				long length = fs.getLength(p);
				System.out.println("length: " + length);
				FSDataInputStream strm = fs.open(p);
				byte [] buf = new byte[sizo]; 
				long total = 0;
				int rd = 0;
				while ( (rd = strm.read(total, buf, 0, sizo)) != -1 )
					   total +=rd;
					   
				System.out.println("read: " + total);
				
				
				while(reader.next(key,cust)) 
				{
				
					// 1. int1
					Integer int1 = cust.GetInt1();
					printField(int1.toString());
					
					// 2. the strings
					String st1 = cust.GetText1();
					printField(st1);
				
					// 3. int2
					Integer int2 = cust.GetInt2();	
					printField(int2.toString());

					// 4. the doubles
					double db = cust.GetDb();
					printField(Double.toString(db));
					
					printField("#############################################################################################");
				}
			
			} 
			catch (EOFException e) 
			{}
			
			z = new Date();
			System.out.println(form.format(z).toString());
		}
		catch (java.io.IOException ie)
		{
		}		
	}
	
	
			
	public static void main(String[] args) throws Exception 
	{ 
		try 
		{ 
			CustomWritableSmallSequence mgr = new CustomWritableSmallSequence(args);
			if (do_write == 0)
			{
				mgr.ReadFile();
			}
			else 
			{
				mgr.WriteFile();
			}
		} 
		finally 
		{ 
		}
		
	} 
}

	























