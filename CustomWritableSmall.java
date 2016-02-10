


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
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.util.Calendar;
import java.util.Date;
import java.sql.Timestamp;


import org.apache.hadoop.io.Writable;

//import com.emc.greenplum.gpdb.hadoop.io.GPDBWritable;



public class CustomWritableSmall implements Writable
{
	public int int1;
	public String text1;
	public int int2;
	public short short1;
	public double db;
	//private boolean setErr = false;
			
	public CustomWritableSmall()
	{
	
		// 1. num1	
		int1 = 0;
		// 2. text1
		text1 = new String("");
		// 3. num2
		int2 = 0;
		// 4. short1
		short1 = 0;
		// 5. double
		db = 0.0;
	}
	
	public CustomWritableSmall(int i1, int i2, int i3)
	{
	
		// 1. num1,num2,short1
		int1   = i1;
		int2   = i2;
		short1 = (short)i1;
		
		// 2. Init strings
		text1 = new String("short_string___" + i1);
		
		// 3. Init doubles
		db = (i3 + 5) * 10.0;

	}
	
	int GetInt1()
	{
		return int1;
	}
	
	int GetInt2()
	{
		return int2;
	}
	
	String GetText1()
	{
		return text1;
	}
	
	double GetDb()
	{
		return db;
	}

	public void write(DataOutput out) throws IOException 
	{
		
		// 1. int1
		IntWritable intw = new IntWritable();
		
		intw.set(int1);
		intw.write(out);
		
		// 2. text1
		Text txt = new Text();
		
		txt.set(text1);
		txt.write(out);
		
		// 3. int2	
		intw.set(int2);
		intw.write(out);
		
		// 4. short1
		ShortWritable shortw = new ShortWritable();

		shortw.set(short1);
		shortw.write(out);

		// 5. doubles
		DoubleWritable dw = new DoubleWritable();
		
		dw.set(db);
		dw.write(out);
		
	}
	
	public void readFields(DataInput in) throws IOException
	{
				
		// 1. int1
		IntWritable intw = new IntWritable();
		
		intw.readFields(in);
		int1 = intw.get();
	
		// 2. text1
		Text txt = new Text();
		
		txt.readFields(in);
		text1 = txt.toString();
			
		// 3. int2	
		intw.readFields(in);
		int2 = intw.get();
		
		// 4. short1
		ShortWritable shortw = new ShortWritable();

		shortw.readFields(in);
		short1 = shortw.get();

		// 5. doubles
		DoubleWritable dw = new DoubleWritable();
		
		dw.readFields(in);
		db = dw.get();
		
	}
	
	public void printFieldTypes()
	{
		Class myClass = this.getClass();
		Field[] fields = myClass.getDeclaredFields();

		for (int i = 0; i < fields.length; i++) 
		{
			System.out.println(fields[i].getType().getName());
		}
	}
}	
	
























