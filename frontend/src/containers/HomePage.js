import React, { useState } from 'react'
import {
  Container,
  Grid,
  makeStyles,
  TextField,
  Button,
  Typography,
  Paper,
  Select,
} from '@material-ui/core';
import { toast } from 'react-toastify';
import { connect } from 'react-redux';
import { createTag } from '../redux/actions/properties';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    direction: 'ltr',
  },
  background: {
    minHeight: `calc(100vh - 5em)`,
  },
  title: {
    fontSize: 90,
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    margin: 'auto',
  },
}))

const Landing = ({ createTag }) => {
  const classes = useStyles();
  const [name, setName] = useState('')

  const handleSubmit = () => {
    if (!name) {
      toast.error('لطفاً عنوان تگ را وارد کن!');
      return;
    }
    createTag(name);
  }

  return (
    <div className={classes.root}>
      <Grid container justify='center' alignItems='center' className={classes.background}>
        <Grid
          xs={10}
          sm={6}
          item container
          justify='center'
          alignItems='stretch'
          direction='column'
          spacing={6}>
          <Grid item>
            <Typography gutterBottom variant='h2' className={classes.title} align='center'>
              بانک مسئله
            </Typography>
          </Grid>
          <Grid item >
            <Grid
              container
              direction='column'
              justify='center'
              spacing={2}>
              <Grid container item alignItems='center' justify='center' spacing={2}>
                <Grid item>
                  <Button size='large' href='/subtag' variant='contained' color='primary'>
                    افزودن ساب‌تگ
                  </Button>
                </Grid>
                <Grid item>
                  <Button size='large' href='/tag' variant='contained' color='primary'>
                    افزودن تگ
                  </Button>
                </Grid>
                <Grid item>
                  <Button size='large' href='/makeproblem' variant='contained' color='primary'>
                    ایجاد سوال
                  </Button>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </div>
  )
}

const mapStateToProps = (state, ownProps) => ({

})

export default connect(
  mapStateToProps,
  {
    createTag,
  }
)(Landing);