


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


public class CustomWritableWithChar implements Writable
{
	public int int1;
	public char char1;
			
	public CustomWritableWithChar()
	{
	
		// 1. num1	
		int1 = 0;
		// 2. char1
		char1 = '\n';
	}
	
	public CustomWritableWithChar(int i1, int i2, int i3)
	{
	
		// 1. num
		int1   = i1;
                char1 = (char)i2;	
	}
	
	int GetInt1()
	{
		return int1;
	}
	
	char GetChar()
	{
		return char1;
	}

	public void write(DataOutput out) throws IOException 
	{
		
		// 1. int1
		IntWritable intw = new IntWritable();
		
		intw.set(int1);
		intw.write(out);
		
	 	// 2. char1
		intw.set(char1);
		intw.write(out);
	}
	
	public void readFields(DataInput in) throws IOException
	{
				
		// 1. int1
		IntWritable intw = new IntWritable();
		
		intw.readFields(in);
		int1 = intw.get();
	
		// 2. char1
		intw.readFields(in);
		char1 = (char)intw.get();
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
	
























